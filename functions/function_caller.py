import types
from functions import get_file_content, get_files_info,  run_python_file, write_file

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