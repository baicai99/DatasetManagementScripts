import os
# 用于给指定文件夹内的所有txt文件添加前缀，记得结尾加逗号。

def add_prefix_to_files(folder_path, prefix):
    # 遍历指定文件夹内的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为txt文件
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # 添加前缀到内容
            new_content = prefix + content
            
            # 将新的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            
            print(f'已处理文件: {filename}')

if __name__ == "__main__":
    folder_path = input("请输入文件夹路径: ")
    prefix = input("请输入要添加的前缀: ")
    add_prefix_to_files(folder_path, prefix)
