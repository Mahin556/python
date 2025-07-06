import shutil
cmd = "ls"
print(shutil.which(cmd))

path="./"
print(shutil.disk_usage(path))

shutil.move()

shutil.make_archive() #Creates an archive (such as AIP or TAR) of a directory and its contents.

shutil.mkdirs() #Creates directories recursively. 

shutil.move('old_name.txt', 'new_name.txt') # rename file or dir
shutil.copy('old_name.txt', 'new_name.txt') # copy file or dir to new file of dir

# Create a ZIP archive
shutil.make_archive('archive_name', 'zip', 'directory_to_archive')

# Extract the archive
shutil.unpack_archive('archive_name.zip', 'extraction_directory')
#Archive Formats Supported
# ZIP, TAR, etc.

# Copy metadata from one file to another
shutil.copystat('source_file.txt', 'destination_file.txt')



# Error handling is an essential aspect of working with file operations. The shutil module provides mechanisms to handle exceptions gracefully. Common errors include FileNotFoundError, PermissionError, and OSError.

# Best Practices for Error Handling:
# Use try-except blocks to catch and handle exceptions.
# Log errors for debugging and monitoring purposes.
# Provide user-friendly error messages.

# FileNotFoundError	Source file/directory not found
# PermissionError	Insufficient permissions for the operation
# OSError	System-related error (e.g., file system issues)

try:
    shutil.copy('nonexistent_file.txt', 'destination/')
except FileNotFoundError as e:
    print(f"Error: {e}")