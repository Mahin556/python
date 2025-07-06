import os

def find_file(file_name):
    list_dir=[
        os.path.dirname(os.path.abspath(__file__)),
        os.path.expanduser("~\\"),
        os.getcwd()
    ]

    for path in list_dir:
        if path is not None:
            file_path=os.path.join(path,file_name)
            print(f"Checking {path}")
            if os.path.exists(file_path):
                return file_path
    
    print(f"{file_name} Not Found!")
    
    

file=find_file("countdown.py")
if file:
    print(f"File Found at:- {file}")