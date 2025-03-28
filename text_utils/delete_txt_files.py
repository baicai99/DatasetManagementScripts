import os

def delete_txt_files(directory):
    """
    删除指定目录及其所有子目录中的所有.txt文件
    
    参数:
        directory (str): 要处理的目录路径
    """
    # 统计删除的文件数量
    deleted_count = 0
    
    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"错误: 目录 '{directory}' 不存在!")
        return
    
    # 遍历目录
    for root, dirs, files in os.walk(directory):
        # 遍历文件
        for file in files:
            # 检查是否为.txt文件
            if file.lower().endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    # 删除文件
                    os.remove(file_path)
                    print(f"已删除: {file_path}")
                    deleted_count += 1
                except Exception as e:
                    print(f"删除失败 {file_path}: {e}")
    
    print(f"\n总共删除了 {deleted_count} 个.txt文件")

if __name__ == "__main__":
    # 获取用户输入的目录
    target_dir = input("请输入要删除.txt文件的目录路径: ")
    
    # 确认用户是否真的要删除文件
    print(f"即将删除目录 '{target_dir}' 及其所有子目录中的所有.txt文件")
    confirmation = input("确定要继续吗? (y/n): ")
    
    if confirmation.lower() == 'y':
        delete_txt_files(target_dir)
    else:
        print("操作已取消")