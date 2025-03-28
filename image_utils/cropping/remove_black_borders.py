import cv2
import numpy as np
import os

def remove_black_borders(image_path, output_path, threshold=10):
    """检测并移除图片的黑色边框"""
    # 读取图像
    img = cv2.imread(image_path)
    
    # 转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 获取非黑色区域的边界
    rows = np.any(gray > threshold, axis=1)
    cols = np.any(gray > threshold, axis=0)
    
    # 找到非黑色区域的边界索引
    top = np.argmax(rows)
    bottom = len(rows) - np.argmax(rows[::-1]) - 1
    left = np.argmax(cols)
    right = len(cols) - np.argmax(cols[::-1]) - 1
    
    # 裁剪图像
    cropped = img[top:bottom+1, left:right+1]
    
    # 保存图像
    cv2.imwrite(output_path, cropped)
    print(f"已处理: {image_path} -> {output_path}")
    
    return cropped

def process_folder(input_folder, output_folder, threshold=10):
    """处理文件夹中的所有图像"""
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)
    
    # 支持的图像格式
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    
    # 处理每个图像文件
    count = 0
    for filename in os.listdir(input_folder):
        # 检查是否为支持的图像格式
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            # 构建完整路径
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # 处理图像
            try:
                remove_black_borders(input_path, output_path, threshold)
                count += 1
            except Exception as e:
                print(f"处理 {filename} 时出错: {e}")
    
    print(f"完成! 共处理了 {count} 张图片")

# 使用方法
if __name__ == "__main__":
    # 设置输入和输出文件夹
    input_folder = r"C:\\Users\\Administrator\\Desktop\\Arcane\\S02E02_sample"  # 修改为您的输入文件夹
    output_folder = r"C:\\Users\\Administrator\\Desktop\\Arcane\\S02E02_sample_removeBorders"  # 修改为您的输出文件夹
    
    # 处理图像
    process_folder(input_folder, output_folder, threshold=10)