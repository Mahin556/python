import os, shutil

# NOTE: You can write every single extensions inside tuples 
extension_list={
    'audio_extensions':('.mp3', '.m4a', '.wav', '.wav', '.flac'),
    'videos_extensions':('mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'documents_extensions':('.doc', '.pdf', '.txt'),
    'images_extensions':('.jpg', '.jpeg', '.png', '.gif', '.tiff', '.tif', '.webp', '.svg','.avif')
}


folder_path=input("Enter a folder path: ")

def file_finder(path, file_extensions):
    # files=[]
    # for file in os.listdir(path):
    #     for extension in file_extensions:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [ file for file in os.listdir(path) for extension in file_extensions if file.endswith(extension) ]

# print(file_finder(folder_path, audio_extensions))

for extension_type, extensions in extension_list.items():
    files_folder_name = extension_type.split('_')[0]+"Files"
    files_folder_path=os.path.join(folder_path,files_folder_name)
    
    if not os.path.exists(files_folder_path) and file_finder(folder_path, extensions):
        os.mkdir(files_folder_path)

    for file in file_finder(folder_path, extensions):
        file_old_path=os.path.join(folder_path, file)
        file_new_path=os.path.join(files_folder_path,file)
        shutil.move(file_old_path,file_new_path)

