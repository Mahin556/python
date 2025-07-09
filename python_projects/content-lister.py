import os

# Take directories from user
# Find if directory exist or not
# Check if you have permission to access the directory
# List file and directories of each directory
# If any error occure give error to user

def find_file(directory):
    try:
       listing=os.listdir(directory)
       return listing, None
    except FileExistsError:
        return None, "Directory Not exist"
    except PermissionError:
        return None, "You don't have proper permissions to access the directory"
    except Exception as e:
        return None, str(e)

def main():
    listing_dir=input("Enter a directories as space seperated:- ").split()
    for dir in listing_dir:
        list_,Error_msg=find_file(dir)
        if list_:
            print(f"Content in ${dir}")
            for i in list_:
                print(i)
            print("-" * 60)
        else:
            print(f"Error in ${dir} => {Error_msg}")
            print("-" * 60)


if __name__ == '__main__':
    main()
