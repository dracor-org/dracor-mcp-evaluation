# Automated Evaluation of the DraCor MCP Server 

The following models were evaluated:
* Sonnet-4
* Haiku-4-5


The script `automatic_prompting.py` was used to perform requests and record the responses. An Anthropic API key is necessary to execute the script.  
The responses of the runs can be found in `results`. For each model, the raw responses are saved in `raw`, the structured responses are saved in `extracted` and the documentation of the runs are saved in `documentation`.

The notebook `Validate_Tool_Chains.ipynb` was used to evaluate the Tool Calling Efficiency metrics. 

In the folder `results_validated` for each models, the evaluated extracted responses are saved:
* `tool_path_length_difference` indicates the Tool-Calling-Complexity
* `absurd_tool_ratio` indicated the Tool-Calling-Absurdity
* `tool_error_rate` indicated the Tool-Calling-Error-Rate


The notebook `responses_analyser.ipynb` was used to analyse the validated results.




