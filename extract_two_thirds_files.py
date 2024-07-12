import os
import shutil
import random

def get_folder_path():
    folder_path = input("请输入文件夹路径: ")
    if not os.path.isdir(folder_path):
        print("无效的文件夹路径，请重新输入。")
        return get_folder_path()
    return folder_path

def extract_two_thirds_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if not files:
        print("文件夹中没有文件。")
        return

    total_files = len(files)
    files_to_extract = random.sample(files, 2 * total_files // 3)

    reg_folder_path = os.path.join(folder_path, "reg")
    os.makedirs(reg_folder_path, exist_ok=True)

    for file_name in files_to_extract:
        shutil.move(os.path.join(folder_path, file_name), os.path.join(reg_folder_path, file_name))

    print(f"已将{len(files_to_extract)}个文件移动到 'reg' 文件夹。")

def main():
    folder_path = get_folder_path()
    extract_two_thirds_files(folder_path)

if __name__ == "__main__":
    main()
