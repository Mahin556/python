import zipfile
import os

# This function can find a files of differnet extensions with in multiple directories
def backup():
    dirs = input("Enter directories to backup (space separated): ").split()
    exts = input("Enter file extensions to include (space separated, e.g. .py .txt): ").split()
    # files_to_compress=[f for ext in exts for dir in dirs for f in os.listdir(dir) if f.endswith(ext)]
    
    files_to_compress=[]

    # prepare list of file to backup
    for dir in dirs:
        if not os.path.isdir(dir):
            print(f"Directory '{dir}' does not exist, skipping.")
            continue

        for file in os.listdir(dir):
            if any(file.endswith(ext) for ext in exts):
                    file_path=os.path.join(dir,file)
                    files_to_compress.append(file_path)
            
        if not os.path.isdir(dir):
            print(f"Directory '{dir}' does not exist, skipping.")
            continue

    # Compress multiple files
    with zipfile.ZipFile('multi_file_archive.zip', 'w') as zipf:
        for file in files_to_compress:
            zipf.write(file, arcname= os.path.basename(file))  # Keep filenames clean

    print(f"{len(files_to_compress)} file(s) backed up to multi_file_archive.zip")

if __name__ == '__main__':
    backup()
    



