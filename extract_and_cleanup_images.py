    # 从源目录中随机提取一定比例的图像文件，并将这些图像文件复制到目标目录，同时删除源目录中对应的图像文件及其同名的.txt文件。

    # 参数:
    # source_dir (str): 源目录路径。
    # target_dir (str): 目标目录路径。
    # percentage (float): 提取图像的比例，默认为0.1（10%）。
    
    # 返回:
    # None

import os
import random
import shutil

def extract_regularization_images(source_dir, target_dir, percentage=0.1):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    num_images_to_extract = int(len(image_files) * percentage)
    
    sampled_images = random.sample(image_files, num_images_to_extract)
    
    for image in sampled_images:
        source_image_path = os.path.join(source_dir, image)
        target_image_path = os.path.join(target_dir, image)
        
        # 复制图像文件
        shutil.copy2(source_image_path, target_image_path)
        
        # 删除源目录中的图像文件
        os.remove(source_image_path)
        
        # 删除对应的 .txt 文件
        txt_file = os.path.splitext(image)[0] + '.txt'
        txt_file_path = os.path.join(source_dir, txt_file)
        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)
    
    print(f"Extracted {num_images_to_extract} images to {target_dir} and deleted corresponding .txt files in the source directory")

# 设置源目录和目标目录路径
source_directory = r"D:\Users\Administrator\Desktop\sakaitakahiro_train\20240628_japcam\images\10_jpcam"
target_directory = r"D:\Users\Administrator\Desktop\sakaitakahiro_train\20240628_japcam\regularization_images"

# 提取10%的图像并删除对应的 .txt 文件和图像文件
extract_regularization_images(source_directory, target_directory, percentage=0.1)
