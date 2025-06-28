import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions import get_files_info, get_file_content, run_python_file, write_file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Check if a command-line argument is provided
if len(sys.argv) < 2:
    print("Error: Please provide a content string.")
    sys.exit(1)

# Get the content string from sys.argv[1]
user_prompts = sys.argv[1]

#System Prompt
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
model_name = 'gemini-2.5-flash'
messages = [types.Content(role="user", parts=[types.Part(text=user_prompts)])]


#Schema for get_files_info
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

#Schema for get_file_content
schema_get_file_content = types.FunctionDeclaration(
    name= "get_file_content",
    description= "Reads and returns the content of a specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type= types.Type.STRING,
                description= "The path of the file to read, relative to the working directory.",
            ),
        },
        required= ["file_path",],
    ),
)

#Schema for run_python_file
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file with optional command-line arguments, and returns its output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                    type=types.Type.STRING,
                    description="The path to the Python file to execute, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)

# Schema for write_file
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites the contents of a specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="The contents to write to the file.",
            ),
        },
        required=["file_path","content"],
    ),
)

#Available functions parameter to pass
# available_functions = types.Tool(function_declarations=[get_file_content_schema_dict])
tools = types.Tool(function_declarations=[schema_get_file_content,
                                          schema_get_files_info,
                                          schema_run_python_file,
                                          schema_write_file])
config = types.GenerateContentConfig(tools=[tools,],
                                     system_instruction=system_prompt)


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    #dictionary of functions
    functions  = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    
    #Check if function name is valid
    function_name = function_call_part.name
    args = dict(function_call_part.args) # or a dict
    args["working_directory"] = "./calculator"

    if function_name not in functions:
        #Error
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                ),
            ],
        )
    
    #Calling function
    actual_function = functions[function_name]
    function_result = actual_function(**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            ),
        ],
    )

#LLM response collected here
response = client.models.generate_content( model=model_name, 
                                          contents=messages,
                                          config=config,)
print("Received response from Gemini API")
# Check for verbose flag
verbose = "--verbose" in sys.argv

# Handle function calls or regular text response
if response.function_calls != []:
    for function_call_part in response.function_calls:
        # Actually call the function instead of just printing
        function_call_result = call_function(function_call_part, verbose)
        
        # Check that the result is valid (as required by lesson)
        if not function_call_result.parts[0].function_response.response:
            raise Exception("Function call failed")
        
        # Print result if verbose
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
else:
    print(response.text)