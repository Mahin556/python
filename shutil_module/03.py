# shutil.copyfile() copies only the file content, not metadata.

# 🔹 Rules:

# Source and destination must both be files (not folders).

# Destination must be writable.

# If destination exists, it gets replaced.

# If source and destination are the same file, it raises an error: SameFileError.

# 🔹 Return:
# Returns the path of the new file created.


import shutil
# Source path 
source = "csv/main.py"

# Destination path 
destination = "csv/gfg/main_2.py"

dest = shutil.copyfile(source, destination) 

print("Destination path:", dest) 