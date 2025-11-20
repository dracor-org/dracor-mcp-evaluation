#!/usr/bin/env python3

import json
import argparse
from pathlib import Path
from typing import Tuple, Union, Any
from pydracor import DraCorAPI
import anthropic
from jsonschema import validate
from datetime import datetime

NUMBER_SCHEMA = {
    "type": "number"
}

STRING_SCHEMA = {
    "type": "string",
    "minLength": 1 
}


def get_dracor_corpora_status():
    dracor = DraCorAPI()
    dracor.get_info()
    corpora = dracor.get_corpora()
    corpus_name_commit = {}
    for corpus in corpora:
        corpus_name_commit[corpus.name] = corpus.commit
    return corpus_name_commit

def document_dracor_status(url:str, start_index:int, runs:int, model:str, max_tokens):
    documentation = get_dracor_corpora_status()
    documentation["server_url"] = url
    documentation["start_index"] = start_index
    documentation["number_of_runs"] = runs,
    documentation["model"] = model
    documentation["max_tokens"] = max_tokens
    documentation["date_time"] = datetime.today().replace(second=0, microsecond=0).isoformat()

    fp = f"{documentation['date_time']}_documentation_runs-{start_index}-{start_index + runs}.log"

    with open(fp, 'w') as docu_out:
        json.dump(documentation, docu_out)


def create_content_schema(question_info: dict[str, Union[str, int]], 
                   validation_data: dict[str, Any]) -> Tuple[str, dict[str,Any]]:
    content = str(question_info["Question"])
    response_type = question_info["Response Type"]
    example = validation_data["example"]
    schema = validation_data["schema"]
    restriction = f"CRITICAL: The answer should be of the data type {response_type}. \
    Do not include any additional explanation, markdown formatting, or text."
    example_mesage = f"Example for an answer is: {example}"
    return " ".join([content, restriction, example_mesage]), schema

# Create message content without validation
def create_content(question_info: dict[str, Union[str, int]]) -> str:
    content = str(question_info["Question"])
    restriction = f"CRITICAL: The answer should be as short and as precise as possible."
    return " ".join([content, restriction])

def create_messsages(questions, validation_data):
    messages_info = []
    for entry in questions:
        if entry["Response Type"] in validation_data:
            selected_validation_data = validation_data[entry["Response Type"]]
            content, schema = create_content_schema(entry, selected_validation_data)
        else:
            content = create_content(entry)
            schema = None
        message = {
            "role": "user",
            "content": content
        }
        messages_info.append({"message":message, "schema":schema, "id":entry["ID"]})
    return messages_info

def isfloat(i: str) -> bool:
    try:
        float(i)
        return True
    except ValueError:
        return False

def perform_request(client: anthropic.Anthropic,
                    message: dict[str, str],
                    server_info: dict,
                    model: str,
                    max_tokens: int):
    response = client.beta.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[message],
        mcp_servers=[
            server_info
        ],
        extra_headers={
            "anthropic-beta": "mcp-client-2025-04-04"
        }
    )
    return response

def process_response(response, schema: dict):
    
    # Extract text
    text_responses = [block.text for block in response.content if block.type == "text"] # this gets all text blocks not only the final one 
    response_text = text_responses[-1].strip() # get final answer

    tools_used = []
    tools_result = {}
    for block in response.content:
        # Check if tool use was successful, did not result in an error
        if block.type == "mcp_tool_result":
            # tool use id mapped to API error (bool)
            tools_result[block.tool_use_id] = block.is_error
        # Extract tools
        # also track IDs to be able to match the tool use with the tool response
        elif block.type == "mcp_tool_use":
            tools_info = {"name": block.name, "input": block.input,"id": block.id}
            tools_used.append(tools_info)
    
    for entry in tools_used:
        if entry["id"] in tools_result:
            entry["is_error"] = tools_result[entry["id"]]

    tool_chain = [entry["name"] for entry in tools_used]
    
    # Get usage info
    usage_infos = {
        "cache_creation_input_tokens": response.usage.cache_creation_input_tokens,
        "cache_read_input_tokens": response.usage.cache_read_input_tokens,
        "input_tokens": response.usage.input_tokens, 
        "output_tokens": response.usage.output_tokens  
    }

    if schema:
        if response_text.isnumeric():
            response_text = int(response_text)
        elif isfloat(response_text):
            response_text = float(response_text)
    
        # Validate
        try:
            # Validate against schema
            validate(instance=response_text, schema=schema)
            valid = True 
        except:
            valid = False
    else:
        valid = None
        
    return {
        "success": True, # if request did not throw an error
        "valid": valid,
        "response": response_text,
        "tools_used": tools_used,
        "tool_chain": tool_chain,
        "usage_infos": usage_infos
    }

def perform_request_runs(messages_info:list[dict[str, Any]], client: anthropic.Anthropic, 
                         server_info:dict[str, str], num_runs: int, start_idx: int, 
                         model: str, max_tokens: int, output_dir:Path):
    # set number of runs
    start = start_idx
    end = start_idx + num_runs + 1

    if not output_dir.exists():
        output_dir.mkdir()

    for i in range(start, end):
        for message_info in messages_info:
            print(f"Question {message_info['id']}, Run: {i}")
            try:
                response = perform_request(client, message_info["message"],server_info, model, max_tokens)
                fp = output_dir / f"{message_info['id']}_{i}_raw.json"
                with open(fp, 'w') as result_out:
                    json.dump(response.to_dict(), result_out)

                extracted_response = process_response(response, message_info["schema"])
            except:
                response = ""
                extracted_response = {
                    "success": False,
                    "valid": False,
                    "response": "",
                    "tools_used": [],
                    "tool_chain": [],
                    "usage_infos":{} 
                }

            # add metdata
            extracted_response["id"] = message_info["id"]
            extracted_response["run"] = i
            extracted_response["datetime"] = datetime.now().isoformat()
             
            # create outputfile for extracted data
            fp_extracted = output_dir / f"{message_info['id']}_{i}_extracted-info.json"
            print(fp_extracted)
            with open(fp_extracted, 'w') as result_out:
                json.dump(extracted_response, result_out)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--question_file', required=True)
    parser.add_argument('--url', default="https://dev.dracor.org/")
    parser.add_argument('--claude-model', default="claude-sonnet-4-20250514")
    parser.add_argument('--max-tokens', default="1024", type=int)
    parser.add_argument('--number-of-runs', default=10, type=int)
    parser.add_argument('--start-index', default="1", type=int)
    parser.add_argument('--document', default=True, type=bool)
    parser.add_argument('--document-dir', default=Path().cwd(), type=Path)
    parser.add_argument('--output-dir', default=Path("results"), type=Path)
    return parser.parse_args()




def main():
    args = _parse_args()

    with open(args.question_file) as question_json:
        questions = json.load(question_json)

    # set client 
    client = anthropic.Anthropic()

    # set server info
    server_info = {
        "type": "url",
        "url": f"{args.url}/mcp/",
        "name": "dracor-mcp",
    }
    validation_data = {
        "int": {
            "example": 5,
            "schema": NUMBER_SCHEMA
        },
        "str": {
            "example": "Emma",
            "schema": STRING_SCHEMA
        },
        "float": {
            "example": 5.0,
            "schema": NUMBER_SCHEMA
        }
    }

    messages = create_messsages(questions, validation_data)
    
    if args.document:
        document_dracor_status(args.url, args.start_index, args.number_of_runs,args.claude_model,args.max_tokens)
    perform_request_runs(messages, client, server_info, args.number_of_runs, args.start_index, args.claude_model, args.max_tokens, args.output_dir)


if __name__ == '__main__':
    main()
