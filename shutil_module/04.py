# shutil.copytree() is used to copy a whole folder (including all files and subfolders) to a new location.

# 🔹 Rules:
# The source must be a folder.
# The destination folder must not exist. It will be created automatically.
# The copy happens recursively (includes everything inside subfolders).
# #shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)

# 🔹 Parameters:
# src: Path of the source folder
# dst: Path where the new folder will be created
# symlinks:
# If True, keeps symbolic links as links
# If False, copies the actual files
# ignore: Optional function to skip certain files or folders
# copy_function:
# By default, uses copy2()
# You can change it to use copy() or copyfile()
# ignore_dangling_symlinks:
# If True, ignores errors when a symlink points to a missing file

# 🔹 Return:
# Returns the path of the new folder created.

import os 
import shutil 

src = 'C:/Users/ksaty/csv/gfg'
dest = 'C:/Users/ksaty/csv/gfg/dest'

destination = shutil.copytree(src, dest) 