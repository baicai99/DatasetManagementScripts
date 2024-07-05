import os
import sys
from PIL import Image, ImageChops, ImageFilter, ImageOps

def trim_white_borders(image, border_color=(255, 255, 255), crop_margin=5):
    # Convert image to RGB if it's not
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Create a new image with the border color
    bg = Image.new('RGB', image.size, border_color)
    
    # Difference image
    diff = ImageChops.difference(image, bg)
    
    # Convert to grayscale
    diff = diff.convert('L')
    
    # Apply a threshold to get a binary image
    threshold = diff.point(lambda p: p > 25 and 255)  # You can adjust the threshold value if needed
    
    bbox = threshold.getbbox()
    if bbox:
        cropped_image = image.crop(bbox)
        # Further crop by the margin from each side
        width, height = cropped_image.size
        final_bbox = (crop_margin, crop_margin, width - crop_margin, height - crop_margin)
        return cropped_image.crop(final_bbox)
    else:
        return image  # No cropping needed

def classify_and_trim_images(input_directory, output_directory, crop_margin=5):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        trimmed_image = trim_white_borders(img, crop_margin=crop_margin)
                        width, height = trimmed_image.size
                        
                        if width > height:
                            size_folder = "横屏"
                        elif width < height:
                            size_folder = "竖屏"
                        else:
                            size_folder = "一比一"
                        
                        target_folder = os.path.join(output_directory, size_folder)
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)
                        
                        trimmed_image.save(os.path.join(target_folder, file))
                        print(f"Processed and saved {file} to {target_folder}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    # Get input directory from user
    input_directory = input("请输入输入文件夹路径：")
    if not os.path.exists(input_directory):
        print("输入文件夹路径不存在，请检查后重新运行脚本。")
        sys.exit(1)
    
    # Get output directory from user
    output_directory = input("请输入输出文件夹路径（默认在父文件夹新建一个'分类结果'文件夹）：")
    if not output_directory:
        output_directory = os.path.join(os.path.dirname(input_directory), "分类结果")

    # Get crop margin from user
    crop_margin_input = input("请输入裁剪的宽高（默认5像素）：")
    crop_margin = int(crop_margin_input) if crop_margin_input else 5

    classify_and_trim_images(input_directory, output_directory, crop_margin)
