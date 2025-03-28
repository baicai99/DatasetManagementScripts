import os
import shutil
from pathlib import Path

def sample_images(input_folder, output_folder, sample_rate=30):
    """
    从输入文件夹中每隔sample_rate张图片采样一张，保存到输出文件夹
    
    参数:
        input_folder: 输入图片文件夹路径
        output_folder: 输出图片文件夹路径
        sample_rate: 采样率，默认为30（每30张采样一张）
    """
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取所有图片文件
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    image_files = []
    
    for file in sorted(os.listdir(input_folder)):
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            # 检查文件扩展名（不区分大小写）
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(file_path)
    
    # 按序号排序（如果文件名包含数字）
    image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x) or '0')) or '0'))
    
    # 采样并复制图片
    sampled_count = 0
    for i, img_path in enumerate(image_files):
        if i % sample_rate == 0:
            # 获取原始文件名
            filename = os.path.basename(img_path)
            # 复制到目标文件夹
            dest_path = os.path.join(output_folder, filename)
            shutil.copy2(img_path, dest_path)
            sampled_count += 1
            print(f"已复制: {filename}")
    
    print(f"完成！从 {len(image_files)} 张图片中采样了 {sampled_count} 张。")

if __name__ == "__main__":
    # 修改这两个路径为您的输入和输出文件夹
    input_folder = r"C:\\Users\\Administrator\\Desktop\\Arcane\\S02E02"
    output_folder = r"C:\\Users\\Administrator\\Desktop\\Arcane\\S02E02_sample"
    
    # 调用函数，每30张图片采样一张
    sample_images(input_folder, output_folder, 100)