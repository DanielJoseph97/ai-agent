import os
#function to read contents of a file
def get_file_content(working_directory, file_path):
    try:
        work_dir = os.path.abspath(working_directory)
        file_path_dir = os.path.abspath(os.path.join(working_directory, file_path))
        if file_path_dir.startswith(work_dir) == False:
            return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

        if os.path.isfile(file_path_dir) == False:
            return f"Error: File not found or is not a regular file: \"{file_path}\""
        
        MAX_CHARS = 10000
        #limit can be set to whatever desired, keeping in mind LLM input tokens
        with open(file_path_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                return file_content_string + f"[...File \"{file_path}\" truncated at 10000 characters]"
            return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"