# #shutil.rmtree() is used to delete a folder and everything inside it (files and subfolders).
# #The path must be a real folder, not a symbolic link.
# #shutil.rmtree(path, ignore_errors=False, onerror=None)
# path: Folder path to delete (string or bytes)
# ignore_errors: If True, it ignores any errors during deletion
# onerror: A custom function that is called if an error happens and ignore_errors is False

import shutil
import os

# full path to folder
path = os.path.join("csv/gfg/", "dest")

# remove folder and all contents
shutil.rmtree(path)

