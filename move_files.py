import os
import shutil

def move_files_to_parent_folder(parent_folder):
    # 遍历父文件夹中的所有项目
    for root, dirs, files in os.walk(parent_folder, topdown=False):
        # 排除父文件夹本身，只处理子文件夹
        if root == parent_folder:
            continue
        
        # 遍历当前子文件夹中的所有文件
        for file_name in files:
            # 构建源文件路径和目标文件路径
            source_file = os.path.join(root, file_name)
            destination_file = os.path.join(parent_folder, file_name)
            
            # 移动文件到父文件夹
            shutil.move(source_file, destination_file)
            print(f"Moved: {source_file} -> {destination_file}")
        
        # 删除空的子文件夹
        os.rmdir(root)
        print(f"Removed empty folder: {root}")

if __name__ == "__main__":
    parent_folder_path = input("请输入父文件夹路径: ")
    if os.path.isdir(parent_folder_path):
        move_files_to_parent_folder(parent_folder_path)
    else:
        print(f"路径无效或不是文件夹: {parent_folder_path}")
