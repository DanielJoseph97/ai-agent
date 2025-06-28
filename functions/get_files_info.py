import os

def get_files_info(working_directory, directory=None):
    try:
        work_dir = os.path.abspath(working_directory)
        if not directory:
             current_dir= work_dir
        else:
            current_dir = os.path.abspath(os.path.join(working_directory, directory))
        
        if current_dir.startswith(work_dir):    
            current_dir_contents = os.listdir(current_dir)
            current_dir_content = []
            
            for item in current_dir_contents:
                    item_path = os.path.join(current_dir, item)
                    item_size = os.path.getsize(item_path)
                    item_dir_check = os.path.isdir(item_path)
                    current_dir_content.append( f"- {item}: file_size={item_size} bytes, is_dir={item_dir_check}")
            dir_content = "\n".join(current_dir_content)
            return dir_content
        else:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    except Exception as e:
        return f"Error: {str(e)}"

