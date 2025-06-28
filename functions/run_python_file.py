import os
import subprocess
from subprocess import PIPE
def run_python_file(working_directory, file_path):
    try:
        if os.path.splitext(file_path)[1] != ".py":
            return f"Error: \"{file_path}\" is not a Python file"
        
        work_dir = os.path.abspath(working_directory)
        file_path_dir = os.path.abspath(os.path.join(working_directory, file_path))
        
        if file_path_dir.startswith(work_dir) == False:
            return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

        if os.path.exists(file_path_dir) == False:
            return f"Error: File \"{file_path}\" not found."

        result = subprocess.run(["python3", file_path_dir], cwd= work_dir, timeout=30, stdout=PIPE, stderr=PIPE)
        result_stdout = result.stdout.decode('utf-8')
        result_stderr = result.stderr.decode('utf-8')
        output_string = ""
        if result_stdout != "":
            output_string += f"STDOUT: {result_stdout} \n"
        if result_stderr != "":
            output_string += f"STDERR: {result_stderr} \n"
        if result.returncode != 0:
            output_string += f"Process exited with code {result.returncode} \n"
        if output_string == "":
            output_string = "No output produced"
            
    except Exception as e:
        return f"Error: executing Python file: {e}"
    return output_string