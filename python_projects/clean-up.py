import os
import shutil

downloads_path = "/path/to/Downloads"

# Create subfolders
os.makedirs(os.path.join(downloads_path, "Images"), exist_ok=True)
os.makedirs(os.path.join(downloads_path, "Documents"), exist_ok=True)
os.makedirs(os.path.join(downloads_path, "Others"), exist_ok=True)

# Organize files
for file in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file)
    if os.path.isfile(file_path):
        if file.endswith((".jpg", ".png", ".gif")):
            shutil.move(file_path, os.path.join(downloads_path, "Images", file))
        elif file.endswith((".txt", ".pdf", ".docx")):
            shutil.move(file_path, os.path.join(downloads_path, "Documents", file))
        else:
            shutil.move(file_path, os.path.join(downloads_path, "Others", file))

print("Downloads folder organized!")