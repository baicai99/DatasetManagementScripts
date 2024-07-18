import os
import shutil
import random

def get_folder_path():
    folder_path = input("请输入文件夹路径: ")
    if not os.path.isdir(folder_path):
        print("无效的文件夹路径，请重新输入。")
        return get_folder_path()
    return folder_path

def get_fraction():
    try:
        numerator = int(input("请输入分子: "))
        denominator = int(input("请输入分母: "))
        if numerator <= 0 or denominator <= 0 or numerator > denominator:
            raise ValueError
        return numerator, denominator
    except ValueError:
        print("无效的输入，请输入正整数且分子不大于分母。")
        return get_fraction()

def extract_fraction_files(folder_path, numerator, denominator):
    # 筛选图片文件
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    files = [f for f in os.listdir(folder_path) 
             if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(image_extensions)]
    
    if not files:
        print("文件夹中没有图片文件。")
        return

    total_files = len(files)
    files_to_extract = random.sample(files, (numerator * total_files) // denominator)

    reg_folder_path = os.path.join(folder_path, "reg")
    os.makedirs(reg_folder_path, exist_ok=True)

    for file_name in files_to_extract:
        shutil.move(os.path.join(folder_path, file_name), os.path.join(reg_folder_path, file_name))

    print(f"已将{len(files_to_extract)}个文件移动到 'reg' 文件夹。")

def main():
    folder_path = get_folder_path()
    numerator, denominator = get_fraction()
    extract_fraction_files(folder_path, numerator, denominator)

if __name__ == "__main__":
    main()
