# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
# from functions import run_python_file

# Commented out sections are from previous chapters in the course, can be removed or ignore
if __name__ == "__main__":
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print( run_python_file("calculator", "main.py"))
    print( run_python_file("calculator", "tests.py"))
    print( run_python_file("calculator", "../main.py"))
    print( run_python_file("calculator", "nonexistent.py"))