import anthropic
import os

url = 'https://dev.dracor.org/'

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What is the number of characters in Der Nollhart? Return only the number, no additional explanation. Example for an answer: 5"}],
    mcp_servers=[
        {
            "type": "url",
            "url": f"{url}/mcp/",
            "name": "dracor-mcp",
        }
    ],
    extra_headers={
        "anthropic-beta": "mcp-client-2025-04-04"
    }
)

print(response.content)

# Extract text and tools
text_responses = [block.text for block in response.content if block.type == "text"]
response_text = text_responses[0].strip()
print(response_text)

tools_used = [
    {"name": block.name, "input": block.input}
    for block in response.content
    if block.type == "mcp_tool_use"
]

print(tools_used)
