import os
import shutil

#Organizing Files by Extension

# Create directories for each file type
os.makedirs("documents", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("archives", exist_ok=True)

# Organize files
for file in os.listdir():
    if file.endswith(".txt") or file.endswith(".docx"):
        shutil.move(file, f"documents/{file}")
    elif file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(file, f"images/{file}")
    elif file.endswith(".zip") or file.endswith(".tar"):
        shutil.move(file, f"archives/{file}")

print("Files organized successfully.")

