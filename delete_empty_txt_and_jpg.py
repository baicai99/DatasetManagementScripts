    # 在指定文件夹中查找所有txt文件，如果txt文件内容为空，则删除该txt文件及其对应的jpg文件。
    
    # 参数:
    # folder_path (str): 要处理的文件夹路径。
    
    # 返回:
    # None

import os

def delete_empty_txt_and_corresponding_jpg(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            txt_path = os.path.join(folder_path, filename)
            jpg_path = os.path.join(folder_path, filename.replace('.txt', '.jpg'))
            
            with open(txt_path, 'r') as file:
                content = file.read().strip()
                
            if not content:  # 如果txt文件为空
                try:
                    os.remove(txt_path)  # 删除txt文件
                    print(f'Deleted: {txt_path}')
                    if os.path.exists(jpg_path):
                        os.remove(jpg_path)  # 删除对应的jpg文件
                        print(f'Deleted: {jpg_path}')
                except Exception as e:
                    print(f"Error deleting files: {e}")

if __name__ == "__main__":
    folder_path = input("请输入文件夹路径：")
    delete_empty_txt_and_corresponding_jpg(folder_path)
    print("处理完成。")
