import os  
from PIL import Image  

def center_crop(image, width, height):  
    img_width, img_height = image.size  
    left = (img_width - width) / 2  
    top = (img_height - height) / 2  
    right = (img_width + width) / 2  
    bottom = (img_height + height) / 2  
    return image.crop((left, top, right, bottom))  

def get_crop_dimensions(image, crop_type):  
    if crop_type == "1":  # 像素裁剪  
        input_width = input("请输入要减去的宽度（像素）：")  
        if input_width == '':  
            print("返回上一级...")  
            return None, None  
        input_height = input("请输入要减去的高度（像素）：")  
        if input_height == '':  
            print("返回上一级...")  
            return None, None  
        width = image.width - int(input_width)  
        height = image.height - int(input_height)  
    elif crop_type == "2":  # 百分比裁剪  
        percent_width = input("请输入要减去的宽度（百分比，例如50表示50%）：")  
        if percent_width == '':  
            print("返回上一级...")  
            return None, None  
        percent_height = input("请输入要减去的高度（百分比，例如50表示50%）：")  
        if percent_height == '':  
            print("返回上一级...")  
            return None, None  
        width = int(image.width * (1 - float(percent_width) / 100))  
        height = int(image.height * (1 - float(percent_height) / 100))  
    else:  
        print("无效的输入，程序结束。")  
        return None, None  
    return width, height  

def crop_and_save_image(image_path, width, height, output_folder):  
    image = Image.open(image_path)  
    cropped_image = center_crop(image, width, height)  

    # 保存结果  
    base_name = os.path.splitext(os.path.basename(image_path))[0]  
    save_path = os.path.join(output_folder, f"{base_name}.png")  
    cropped_image.save(save_path)  
    print(f"图片已保存到 {save_path}")  

def main():  
    print("请选择裁剪方式：")  
    print("1: 像素")  
    print("2: 百分比")  
    crop_type = input("请输入1或2选择裁剪方式：").strip()  
    if crop_type == "":  
        print("返回上一级...")  
        return  

    folder_path = input("请输入文件夹路径：").strip()  
    if folder_path == "":  
        print("返回上一级...")  
        return  

    # 询问用户输出文件夹路径
    output_folder = input("请输入输出文件夹路径（留空则默认为当前目录下的cropped_images）：").strip()
    if output_folder == "":
        output_folder = os.path.join(folder_path, "cropped_images")
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹并处理图片  
    # 默认第一张图片用于获取裁剪参数  
    for file_name in os.listdir(folder_path):  
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  
            image_path = os.path.join(folder_path, file_name)  
            image = Image.open(image_path)  

            # 获取宽度和高度  
            width, height = get_crop_dimensions(image, crop_type)  
            if width is None or height is None:  
                return  # 如果返回上一级则退出  

            # 对文件夹内的每个图像进行裁剪并保存  
            crop_and_save_image(image_path, width, height, output_folder)  
            break  # 只使用第一张图片来获取裁剪尺寸  

    # 处理完裁剪尺寸后，继续处理所有图片  
    for file_name in os.listdir(folder_path):  
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  
            image_path = os.path.join(folder_path, file_name)  
            crop_and_save_image(image_path, width, height, output_folder)  

if __name__ == "__main__":  
    main()
