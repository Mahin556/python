import os

def find_file(file_name):
    current_directory=os.getcwd()
    file_path=os.path.join(current_directory,file_name)
    if os.path.exists(file_path):
        return file_path
    
    user_home=os.path.expanduser("~/")
    file_path=os.path.join(user_home,file_name)
    if os.path.exists(file_path):
        return file_path
    
    script_dir=os.path.abspath(__file__)
    file_path=os.path.join(script_dir,file_name)
    if os.path.exists(file_path):
        return file_path
    
    print(f"{file_name} Not Found!")

file=find_file("countdown.py")
if file:
    print(f"{file} Found")