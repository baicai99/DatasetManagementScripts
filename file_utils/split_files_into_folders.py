import os
import shutil

def get_folder_path():
    folder_path = input("请输入文件夹路径: ")
    if not os.path.isdir(folder_path):
        print("无效的文件夹路径，请重新输入。")
        return get_folder_path()
    return folder_path

def get_files_per_folder():
    try:
        files_per_folder = int(input("请输入每个文件夹的文件数量: "))
        if files_per_folder <= 0:
            raise ValueError
    except ValueError:
        print("无效的输入，请输入一个正整数。")
        return get_files_per_folder()
    return files_per_folder

def split_files_into_folders(folder_path, files_per_folder):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    total_files = len(files)
    total_folders = (total_files // files_per_folder) + (1 if total_files % files_per_folder else 0)

    for i in range(total_folders):
        new_folder_path = os.path.join(folder_path, f"folder_{i+1}")
        os.makedirs(new_folder_path, exist_ok=True)
        
        start_index = i * files_per_folder
        end_index = start_index + files_per_folder
        files_to_move = files[start_index:end_index]
        
        for file_name in files_to_move:
            shutil.move(os.path.join(folder_path, file_name), os.path.join(new_folder_path, file_name))

def main():
    folder_path = get_folder_path()
    files_per_folder = get_files_per_folder()
    split_files_into_folders(folder_path, files_per_folder)
    print("文件切分并重新组织完成。")

if __name__ == "__main__":
    main()
