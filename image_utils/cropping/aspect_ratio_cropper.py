from PIL import Image
import os
import glob

def center_crop_ratio(image_path, output_path, width_ratio, height_ratio):
    """
    对图像进行中心裁剪，使其满足指定的宽高比例
    
    参数:
        image_path: 输入图像的路径
        output_path: 输出图像的路径
        width_ratio: 宽度比例
        height_ratio: 高度比例
    """
    try:
        # 打开图像
        img = Image.open(image_path)
        width, height = img.size
        
        # 计算目标宽高比
        target_ratio = width_ratio / height_ratio
        
        # 计算当前宽高比
        current_ratio = width / height
        
        if current_ratio > target_ratio:
            # 当前图像过宽，需要裁剪宽度
            new_width = int(height * target_ratio)
            left = (width - new_width) // 2
            right = left + new_width
            img_cropped = img.crop((left, 0, right, height))
        else:
            # 当前图像过高，需要裁剪高度
            new_height = int(width / target_ratio)
            top = (height - new_height) // 2
            bottom = top + new_height
            img_cropped = img.crop((0, top, width, bottom))
        
        # 保存裁剪后的图像
        img_cropped.save(output_path)
        print(f"裁剪完成: {os.path.basename(output_path)}")
        return True
    except Exception as e:
        print(f"处理图像 {os.path.basename(image_path)} 时出错: {e}")
        return False

def process_folder(input_folder, output_folder, width_ratio, height_ratio):
    """
    处理文件夹中的所有图像
    
    参数:
        input_folder: 输入图像的文件夹路径
        output_folder: 输出图像的文件夹路径
        width_ratio: 宽度比例
        height_ratio: 高度比例
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取所有图像文件
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.gif', '*.webp']
    image_files = []
    
    for ext in image_extensions:
        pattern = os.path.join(input_folder, ext)
        image_files.extend(glob.glob(pattern))
        # 同时查找子文件夹中的图像（不区分大小写）
        pattern = os.path.join(input_folder, ext.upper())
        image_files.extend(glob.glob(pattern))
    
    if not image_files:
        print(f"在 {input_folder} 中没有找到图像文件")
        return
    
    # 处理每个图像文件
    successful = 0
    for image_path in image_files:
        # 创建输出路径
        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_{width_ratio}x{height_ratio}{ext}"
        output_path = os.path.join(output_folder, new_filename)
        
        # 处理图像
        if center_crop_ratio(image_path, output_path, width_ratio, height_ratio):
            successful += 1
    
    print(f"\n处理完成! 共处理 {len(image_files)} 个文件，成功 {successful} 个。")
    print(f"裁剪后的图像已保存到: {output_folder}")

def get_valid_number(prompt):
    """获取有效的正整数输入"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("请输入大于0的正整数。")
                continue
            return value
        except ValueError:
            print("无效输入，请输入一个正整数。")

if __name__ == "__main__":
    # 用户输入
    input_folder = input("请输入原始图像所在文件夹路径: ")
    output_folder = input("请输入裁剪后图像保存文件夹路径: ")
    
    # 获取宽高比例
    print("\n请输入目标宽高比例（例如，16:9 请分别输入 16 和 9）")
    width_ratio = get_valid_number("宽度比例: ")
    height_ratio = get_valid_number("高度比例: ")
    
    print(f"\n将按照 {width_ratio}:{height_ratio} 的比例进行中心裁剪")
    
    # 执行裁剪
    process_folder(input_folder, output_folder, width_ratio, height_ratio)