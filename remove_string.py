import os

def remove_string_from_files(folder_path, string_to_remove):
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        print(f"错误：文件夹 '{folder_path}' 不存在！")
        return

    # 遍历文件夹中的所有文件
    txt_files_count = 0
    modified_files_count = 0
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            # 检查是否为txt文件
            if file.lower().endswith('.txt'):
                txt_files_count += 1
                file_path = os.path.join(root, file)
                try:
                    # 读取文件内容
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 检查文件中是否包含要删除的字符串
                    if string_to_remove in content:
                        # 删除字符串
                        new_content = content.replace(string_to_remove, '')
                        
                        # 写回文件
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        modified_files_count += 1
                        print(f"已处理文件: {file_path}")
                except Exception as e:
                    print(f"处理文件 '{file_path}' 时出错: {str(e)}")
    
    print(f"\n处理完成！")
    print(f"共扫描了 {txt_files_count} 个txt文件")
    print(f"修改了 {modified_files_count} 个文件")

def main():
    print("=== 文本文件字符串删除工具 ===")
    folder_path = input("请输入要处理的文件夹路径: ")
    string_to_remove = input("请输入要删除的字符串: ")
    
    print(f"\n开始处理文件夹: {folder_path}")
    print(f"要删除的字符串: '{string_to_remove}'")
    
    confirm = input("\n确认要继续吗？(y/n): ")
    if confirm.lower() == 'y':
        remove_string_from_files(folder_path, string_to_remove)
    else:
        print("操作已取消")

if __name__ == "__main__":
    main()