import os
from PIL import Image
import math
import imghdr

def is_valid_image(file_path):
    """检查文件是否为有效的图片文件"""
    try:
        img_type = imghdr.what(file_path)
        if img_type is None:
            return False
            
        with Image.open(file_path) as img:
            img.verify()
        return True
    except:
        return False

def compress_image(input_path, max_size_kb):
    if not is_valid_image(input_path):
        raise ValueError(f"文件不是有效的图片: {input_path}")
    
    img = Image.open(input_path)
    
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    width, height = img.size
    current_size = os.path.getsize(input_path)
    
    if current_size <= max_size_kb * 1024:
        print(f"文件已经小于{max_size_kb}KB，跳过压缩: {input_path}")
        return
        
    scale = math.sqrt((max_size_kb * 1024) / current_size)
    new_width = int(width * scale)
    new_height = int(height * scale)
    
    print(f"压缩 {input_path}")
    print(f"原始大小: {current_size/1024:.2f}KB")
    print(f"原始尺寸: {width}x{height}")
    print(f"新尺寸: {new_width}x{new_height}")
    
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    if resized_img.mode == 'RGBA':
        resized_img = resized_img.convert('RGB')
    
    resized_img.save(input_path, quality=95, optimize=True)
    
    final_size = os.path.getsize(input_path)
    print(f"压缩后大小: {final_size/1024:.2f}KB")
    print("------------------------")

def process_directory(directory, max_size_kb):
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    
    if not os.path.exists(directory):
        print(f"目录不存在: {directory}")
        return
        
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_extensions):
                file_path = os.path.join(root, file)
                try:
                    compress_image(file_path, max_size_kb)
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {str(e)}")
                    print("------------------------")

def main():
    directory_path = input("请输入图片目录路径: ").strip()
    while True:
        try:
            max_size_kb = int(input("请输入目标压缩大小(KB): ").strip())
            if max_size_kb > 0:
                break
            print("请输入大于0的数字")
        except ValueError:
            print("请输入有效的数字")
    
    process_directory(directory_path, max_size_kb)

if __name__ == "__main__":
    main()