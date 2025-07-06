# # import shutil

# # #shutil.which() is used to find the full path of a program (executable) available in the system's PATH.
# # # shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)

# # cmd: Name of the program (as a string)

# # mode:

# # os.F_OK: Check if the file exists

# # os.X_OK: Check if the file is executable

# # path:

# # Custom path to search (optional)

# # If not given, it uses the system PATH


#  Return:
# Returns the full path to the executable if found, otherwise returns None.

import shutil

cmd = 'ls'
locate = shutil.which(cmd)
print(locate)