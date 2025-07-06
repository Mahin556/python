import os
import shutil
from datetime import datetime

# Create backup folder with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = f"backup_{timestamp}"
os.makedirs(backup_folder)

# Backup .py files
for file in os.listdir():
    if file.endswith(".py"):
        shutil.copy(file, os.path.join(backup_folder, file))

print(f"Backup completed in {backup_folder}.")