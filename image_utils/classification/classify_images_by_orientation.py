import os
import shutil
from PIL import Image
import time

def get_folder_path():
    folder_path = input("请输入文件夹路径: ")
    if not os.path.isdir(folder_path):
        print("无效的文件夹路径，请重新输入。")
        return get_folder_path()
    return folder_path

def move_file_with_retry(src, dest, retries=3, delay=1):
    for _ in range(retries):
        try:
            shutil.move(src, dest)
            return True
        except Exception as e:
            print(f"无法移动文件 {src}: {e}")
            time.sleep(delay)
    return False

def categorize_images_by_orientation(folder_path):
    landscape_folder = os.path.join(folder_path, "landscape")
    portrait_folder = os.path.join(folder_path, "portrait")
    square_folder = os.path.join(folder_path, "square")

    os.makedirs(landscape_folder, exist_ok=True)
    os.makedirs(portrait_folder, exist_ok=True)
    os.makedirs(square_folder, exist_ok=True)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                if width > height:
                    move_file_with_retry(file_path, os.path.join(landscape_folder, file_name))
                elif height > width:
                    move_file_with_retry(file_path, os.path.join(portrait_folder, file_name))
                else:
                    move_file_with_retry(file_path, os.path.join(square_folder, file_name))
            except Exception as e:
                print(f"无法处理文件 {file_name}: {e}")

    print("图片已分类并移动到对应文件夹。")

def main():
    folder_path = get_folder_path()
    categorize_images_by_orientation(folder_path)

if __name__ == "__main__":
    main()
