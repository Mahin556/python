import zipfile

# Compress a single file
with zipfile.ZipFile('my_archive.zip', 'w') as zipf:
    zipf.write('file_to_compress.txt', arcname='renamed_file.txt') 
    # arcname allows you to specify the name inside the archive

# Compress multiple files
files_to_compress = ['file1.txt', 'file2.txt']
with zipfile.ZipFile('multi_file_archive.zip', 'w') as zipf:
    for file in files_to_compress:
        zipf.write(file)

# Extracting files from a ZIP archive
with zipfile.ZipFile('my_archive.zip', 'r') as zipf:
    zipf.extractall('extracted_folder') 
    # Extracts all contents to a specified folder


import shutil

# Compress a directory into a ZIP archive
shutil.make_archive('my_folder_archive', 'zip', 'path/to/my_folder')

# Compress a directory into a gzipped tar archive
shutil.make_archive('my_folder_archive', 'gztar', 'path/to/my_folder')


import tarfile

# Create a gzipped tar archive from a directory
with tarfile.open('my_tar_gz_archive.tar.gz', 'w:gz') as tar:
    tar.add('path/to/my_folder', arcname='my_folder_in_archive')

# Extracting files from a gzipped tar archive
with tarfile.open('my_tar_gz_archive.tar.gz', 'r:gz') as tar:
    tar.extractall('extracted_from_tar')


