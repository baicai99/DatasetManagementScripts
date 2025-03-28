import os
import shutil

def rename_files_in_folders(root_directory):
    """
    遍历指定目录及其所有子目录，在每个文件夹中单独对文件重命名，从1开始累加
    
    参数:
        root_directory (str): 要处理的根目录路径
    """
    # 检查目录是否存在
    if not os.path.exists(root_directory):
        print(f"错误: 目录 '{root_directory}' 不存在!")
        return
    
    # 统计总共重命名的文件数量
    total_renamed = 0
    
    # 遍历目录树
    for current_dir, subdirs, files in os.walk(root_directory):
        print(f"\n处理目录: {current_dir}")
        
        # 如果当前目录没有文件，继续下一个目录
        if not files:
            print(f"  目录为空，跳过")
            continue
        
        # 获取当前目录中的所有文件并排序
        files_in_dir = [f for f in files if os.path.isfile(os.path.join(current_dir, f))]
        files_in_dir.sort()
        
        # 重命名计数器从1开始
        counter = 1
        renamed_in_current_dir = 0
        
        # 暂存重命名映射，用于避免重命名冲突
        rename_map = {}
        
        # 构建重命名映射
        for file in files_in_dir:
            file_path = os.path.join(current_dir, file)
            
            # 获取文件扩展名
            filename, extension = os.path.splitext(file)
            
            # 新文件名：数字序号+原扩展名
            new_name = f"{counter}{extension}"
            new_path = os.path.join(current_dir, new_name)
            
            # 存储重命名映射
            rename_map[file_path] = new_path
            counter += 1
        
        # 执行重命名操作
        for old_path, new_path in rename_map.items():
            try:
                filename = os.path.basename(old_path)
                new_name = os.path.basename(new_path)
                
                # 如果新文件名已存在，使用临时名称
                if os.path.exists(new_path):
                    temp_path = old_path + ".temp"
                    shutil.move(old_path, temp_path)
                    old_path = temp_path
                
                # 重命名文件
                shutil.move(old_path, new_path)
                print(f"  已重命名: {filename} -> {new_name}")
                renamed_in_current_dir += 1
                total_renamed += 1
            except Exception as e:
                print(f"  重命名失败 {filename}: {e}")
        
        print(f"  在此目录中重命名了 {renamed_in_current_dir} 个文件")
    
    print(f"\n总共重命名了 {total_renamed} 个文件")

if __name__ == "__main__":
    # 获取用户输入的目录
    directory = input("请输入要处理的目录路径: ")
    
    # 确认用户是否真的要重命名文件
    print(f"即将在目录 '{directory}' 及其所有子目录中重命名文件")
    confirmation = input("此操作不可逆，确定要继续吗? (y/n): ")
    
    if confirmation.lower() == 'y':
        rename_files_in_folders(directory)
    else:
        print("操作已取消")