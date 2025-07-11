import os

def create_file(filename):
    try:
        with open(filename,"x") as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(f"File name {filename} already exists!!")
    except Exception as E:
        print(f"A error occurred!!!")

def view_files():
    files=os.listdir()
    if not files:
        print("No file found!")
    else:
        print("Files in directory")
        for file in files:
            print(file)
        
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File Name {filename}: Deleted Successfully!")
    except FileNotFoundError:
        print("File not exist!!")
    except Exception as E:
        print("An Error occurred!!!")

def read_file(filename):
    try:
        with open(filename,"r") as f:
            content=f.read()
            print(f"----- File Name:- {filename} content -----\n{content}")
    except FileNotFoundError:
        print(f"File Name {filename} not exist!")
    except Exception as E:
        print("An Error Occurred")

def update_file(filename):
    try:
        with open(filename,"a") as file:
            to_add=input("Enter a content to add:- ")
            file.write(to_add + '\n')
            print(f"Content added to file name {filename} Successfully!")
    except FileNotFoundError:
        print(f"File Name {filename} not exist!")
    except Exception as E:
        print("An Error Occurred")

def main():
    while True:
        print(f"FILE MANAGEMENT SYSTEM")
        print(f"1: Create File")
        print(f"2: View all Files")
        print(f"3: Delete File")
        print(f"4: Read File")
        print(f"5: Edit File")
        print(f"6: Exit")

        choice = int(input("Enter your choice:- "))
        match choice:
            case 1: 
                filename=input("Enter a file name to create:- ")
                create_file(filename)
            case 2: 
                view_files()
            case 3: 
                filename=input("Enter a file name to delete:- ")
                delete_file(filename)
            case 4: 
                filename=input("Enter a file name to read:- ")
                read_file(filename)
            case 5: 
                filename=input("Enter a file name to update:- ")
                update_file(filename)
            case 6: 
                print("Closing the app......")
                break
            case _: 
                print("Invalid Syntax")

if __name__ == '__main__':
    main()



        
