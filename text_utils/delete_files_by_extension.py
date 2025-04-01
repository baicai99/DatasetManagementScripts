import os

def delete_files_by_extension(directory, extension='.npz', recursive=True):
    """
    删除指定目录中的所有指定扩展名文件
    
    参数:
        directory (str): 要处理的目录路径
        extension (str): 要删除的文件扩展名，例如'.npz'
        recursive (bool): 是否递归处理子文件夹
    """
    # 统计删除的文件数量
    deleted_count = 0
    
    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 '{directory}' 不存在!")
        return
    
    if recursive:
        # 递归遍历目录及子目录
        for root, dirs, files in os.walk(directory):
            # 遍历文件
            for file in files:
                # 检查是否为指定扩展名文件
                if file.lower().endswith(extension):
                    file_path = os.path.join(root, file)
                    try:
                        # 删除文件
                        os.remove(file_path)
                        print(f"已删除: {file_path}")
                        deleted_count += 1
                    except Exception as e:
                        print(f"删除失败 {file_path}: {e}")
    else:
        # 只处理当前目录
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            # 只处理文件，不处理文件夹
            if os.path.isfile(file_path) and file.lower().endswith(extension):
                try:
                    # 删除文件
                    os.remove(file_path)
                    print(f"已删除: {file_path}")
                    deleted_count += 1
                except Exception as e:
                    print(f"删除失败 {file_path}: {e}")
    
    print(f"\n总共删除了 {deleted_count} 个{extension}文件")

if __name__ == "__main__":
    # 获取用户输入的目录
    target_dir = input("请输入要删除文件的目录路径: ")
    
    # 获取用户想要删除的文件扩展名
    file_extension = input("请输入要删除的文件扩展名(例如 .npz): ")
    if not file_extension.startswith('.'):
        file_extension = '.' + file_extension
    
    # 询问是否递归处理子文件夹
    recursive_option = input("是否需要遍历子文件夹? (y/n): ")
    recursive = recursive_option.lower() == 'y'
    
    # 确认用户是否真的要删除文件
    if recursive:
        print(f"即将删除目录 '{target_dir}' 及其所有子文件夹中的所有{file_extension}文件")
    else:
        print(f"即将仅删除目录 '{target_dir}' 中的所有{file_extension}文件，不处理子文件夹")
    
    confirmation = input("确定要继续吗? (y/n): ")
    
    if confirmation.lower() == 'y':
        delete_files_by_extension(target_dir, file_extension, recursive)
    else:
        print("操作已取消")