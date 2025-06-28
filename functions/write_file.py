import os
def write_file(working_directory, file_path, content):
    try:
        work_dir = os.path.abspath(working_directory)
        file_path_dir = os.path.abspath(os.path.join(working_directory, file_path))

        if file_path_dir.startswith(work_dir) == False:
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

        parent_dir = os.path.dirname(file_path_dir)
        os.makedirs(parent_dir, exist_ok=True) 

        with open(file_path_dir, "w") as f:
            f.write(content)
            return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: {str(e)}"