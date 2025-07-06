# # shutil.copy2() copies a file along with its metadata (like creation and modification times).

# # 🔹 Difference from shutil.copy():
# # It does the same work, but also keeps file metadata.

# 🔹 Return:
# Returns the path of the new copied file.

import shutil
src="src/file1"
dest="dest/"

dest_path = shutil.copy2(src,dest)
print(dest_path)