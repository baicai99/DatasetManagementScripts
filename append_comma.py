import os

def append_text_to_txt_files(folder_path, text_to_append):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    
    for file_name in files:
        # 过滤出所有的txt文件
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            try:
                # 打开文件，读取内容并添加指定的文本
                with open(file_path, 'a', encoding='utf-8') as file:
                    file.write(text_to_append)
                print(f"添加 '{text_to_append}' 到文件: {file_name}")
            except Exception as e:
                print(f"处理文件 {file_name} 时出错: {e}")

if __name__ == "__main__":
    # 询问用户输入文件夹路径
    folder_path = input("请输入文件夹路径: ")
    # 询问用户需要追加的文本
    text_to_append = input("请输入需要追加的文本: ")
    append_text_to_txt_files(folder_path, text_to_append)
