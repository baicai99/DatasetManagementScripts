import os
import shutil

def get_folder_path():
    folder_path = input("请输入文件夹路径: ")
    if not os.path.isdir(folder_path):
        print("无效的文件夹路径，请重新输入。")
        return get_folder_path()
    return folder_path

def extract_all_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, os.path.join(folder_path, file))
    
    # 清理空文件夹
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

def main():
    folder_path = get_folder_path()
    extract_all_files(folder_path)
    print("所有文件提取完成并移至根文件夹。")

if __name__ == "__main__":
    main()
