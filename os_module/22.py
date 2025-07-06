import os

def find_file(file_name):
    current_dir=os.getcwd()
    file_path=os.path.join(current_dir,file_name)

    if os.path.exists(file_path):
        return f"{file_path} exist in current directory({current_dir})"
    return f"{file_path} not exist in current directory({current_dir})"
    
print(find_file("countdown.py"))


# os.path.expanduser()
# When os.path.expanduser() encounters a tilde character (~) at the beginning of a path, it replaces it with the absolute path to the current user's home directory.


def find_file_home(file_name):
    user_dir=os.path.expanduser("~/")
    file_path=os.path.join(user_dir,file_name)

    if os.path.exists(file_path):
        return f"{file_name} exist in user's home directory({user_dir})"
    return f"{file_path} not exist in user's home directory({user_dir})"

print(find_file_home("countdown.py"))

def find_file_script(file_name):
    script_path = os.path.abspath(__file__)
    parent_path=os.path.dirname(script_path)
    file_path=os.path.join(parent_path,file_name)
    if not os.path.exists(file_path):
        return f"{file_path} not exist in script directory({script_path})"
    return f"{file_path} exist in script directory({script_path})"

