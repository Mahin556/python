import shutil

# shutil.copy() is used to copy a file from one place to another in Python.

# 🔹 What it copies:
# It copies the file content and permissions.
# It does not copy creation or modification times.

# 🔹 Source and destination:
# Source must be a file.
# Destination can be a file or folder.
# If it’s a folder, the file goes inside it.
# If a file already exists there, it gets replaced.
# If not, a new file is created.

# return a file destination path
#shutil.copy(source, destination, follow_symlinks=True)

src="src/file1"
dest="dest/"

dest_path = shutil.copy(src,dest)
print(dest_path)
    