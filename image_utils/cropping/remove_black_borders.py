import cv2
import numpy as np
import os
import sys # 导入sys模块用于退出

def remove_black_borders(image_path, output_path, threshold=10):
    """
    检测并移除单张图片的黑色边框。

    参数:
        image_path (str): 输入图片路径。
        output_path (str): 输出图片路径。
        threshold (int): 判断是否为黑色的阈值 (0-255)。低于此值的像素被认为是黑色。

    返回:
        bool: 处理是否成功。
    """
    # 读取图像
    img = cv2.imread(image_path)

    # 检查图像是否成功读取
    if img is None:
        print(f"错误：无法读取图像文件: {image_path}")
        return False

    # 获取图像尺寸
    original_height, original_width = img.shape[:2]

    # 转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --- 查找非黑色区域边界 ---
    # 检查行：如果一行中所有像素值都 <= threshold，则认为它是黑边部分
    # np.any(gray > threshold, axis=1) 找到至少包含一个非黑像素的行
    rows_with_content = np.where(np.any(gray > threshold, axis=1))[0]
    # 检查列：类似地找到至少包含一个非黑像素的列
    cols_with_content = np.where(np.any(gray > threshold, axis=0))[0]

    # 如果图像完全是黑色（或低于阈值），或者找不到内容区域
    if rows_with_content.size == 0 or cols_with_content.size == 0:
        print(f"警告：在 {os.path.basename(image_path)} 中未检测到高于阈值 {threshold} 的内容区域。可能整张图都是黑边或颜色很深。将复制原图。")
        try:
            shutil.copy2(image_path, output_path) # 复制原图（保留元数据）
            return True # 认为处理（复制）成功
        except Exception as e:
            print(f"错误：复制原图 {os.path.basename(image_path)} 时失败: {e}")
            return False

    # 获取内容区域的边界
    top = rows_with_content.min()
    bottom = rows_with_content.max()
    left = cols_with_content.min()
    right = cols_with_content.max()

    # --- 裁剪图像 ---
    # 加1是因为切片是不包含结束索引的
    cropped = img[top:bottom+1, left:right+1]

    # 获取裁剪后尺寸
    cropped_height, cropped_width = cropped.shape[:2]

    # 检查裁剪后的图像是否有效（有时极端情况下可能裁剪出空图像）
    if cropped_height <= 0 or cropped_width <= 0:
        print(f"警告：在 {os.path.basename(image_path)} 中计算出的裁剪区域无效。将复制原图。")
        try:
            shutil.copy2(image_path, output_path)
            return True
        except Exception as e:
            print(f"错误：复制原图 {os.path.basename(image_path)} 时失败: {e}")
            return False

    # --- 保存图像 ---
    try:
        success = cv2.imwrite(output_path, cropped)
        if not success:
             print(f"错误：保存裁剪后的图像失败: {output_path}")
             return False
        # 可选：打印尺寸变化
        # print(f"已处理: {os.path.basename(image_path)} ({original_width}x{original_height} -> {cropped_width}x{cropped_height}) -> {os.path.basename(output_path)}")
    except Exception as e:
        print(f"错误：保存图像 {output_path} 时发生异常: {e}")
        return False

    return True

def process_folder(input_folder, output_folder, threshold=10):
    """
    处理指定文件夹中的所有支持格式的图像，移除黑边。

    参数:
        input_folder (str): 输入文件夹路径。
        output_folder (str): 输出文件夹路径。
        threshold (int): 黑边检测阈值。
    """
    # --- 文件夹检查和创建 ---
    if not os.path.isdir(input_folder):
        print(f"错误：输入文件夹不存在或不是有效目录: {input_folder}")
        return

    try:
        # 确保输出文件夹存在
        os.makedirs(output_folder, exist_ok=True)
    except OSError as e:
        print(f"错误：无法创建或访问输出文件夹 {output_folder}。原因: {e}")
        return

    # --- 文件处理 ---
    print(f"开始处理文件夹: {input_folder}")
    print(f"使用阈值: {threshold}")
    # 支持的图像格式 (小写)
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    processed_count = 0
    failed_count = 0

    try:
        all_files = os.listdir(input_folder)
    except OSError as e:
        print(f"错误：无法读取输入文件夹内容 {input_folder}。原因: {e}")
        return

    total_files = len(all_files)
    print(f"共找到 {total_files} 个文件/文件夹，开始筛选图片...")

    # 使用 tqdm 添加进度条 (可选, 如果文件多的话体验更好)
    try:
        from tqdm import tqdm
        iterator = tqdm(all_files, desc="处理图片", unit="张")
    except ImportError:
        print("(提示: 可以安装 'tqdm' 库以显示进度条: pip install tqdm)")
        iterator = all_files # 没有tqdm就直接迭代

    for filename in iterator:
        # 检查是否为支持的图像格式
        file_lower = filename.lower()
        if any(file_lower.endswith(ext) for ext in image_extensions):
            # 构建完整路径
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename) # 输出文件名保持一致

            # 确保是文件而不是目录（虽然上层检查过，多一层保险）
            if not os.path.isfile(input_path):
                 continue

            # 处理图像
            if remove_black_borders(input_path, output_path, threshold):
                processed_count += 1
            else:
                failed_count += 1
                # 可以在进度条上显示失败信息
                if 'iterator' in locals() and hasattr(iterator, 'set_postfix'):
                    iterator.set_postfix(失败=failed_count)


    print(f"\n处理完成!")
    print(f"成功处理: {processed_count} 张图片")
    if failed_count > 0:
        print(f"处理失败: {failed_count} 张图片 (详情请查看上面的错误信息)")
    print(f"结果已保存到: {output_folder}")

def get_user_input_borders():
    """获取用户输入的黑边移除参数"""
    while True:
        input_folder = input("请输入包含图片的源文件夹路径: ").strip().strip('"').strip("'")
        if os.path.isdir(input_folder): # 检查是否是目录
            break
        else:
            print("错误：输入的路径不存在或不是一个有效的文件夹，请重新输入。")

    while True:
        output_folder = input("请输入保存处理后图片的目标文件夹路径: ").strip().strip('"').strip("'")
        if output_folder:
            # 检查路径是否是文件
            if os.path.exists(output_folder) and not os.path.isdir(output_folder):
                 print(f"错误：输出路径 '{output_folder}' 已存在但不是一个文件夹，请选择其他路径。")
            # 检查路径是否存在且非空
            elif os.path.exists(output_folder) and os.listdir(output_folder):
                 confirm_overwrite = input(f"警告：输出文件夹 '{output_folder}' 已存在且包含文件，继续操作可能会覆盖同名文件。是否继续? (y/n): ").lower().strip()
                 if confirm_overwrite == 'y':
                     break
                 else:
                     print("操作已取消，请选择新的输出文件夹。")
            # 路径不存在或是空文件夹，则允许
            else:
                break
        else:
             print("错误：输出文件夹路径不能为空，请重新输入。")

    while True:
        try:
            threshold_str = input("请输入黑边检测阈值 (0-255，像素值低于此值视为黑色，默认为 10): ").strip()
            if not threshold_str: # 用户直接回车，使用默认值
                threshold = 10
            else:
                threshold = int(threshold_str)
            # 确保阈值在合理范围内
            if 0 <= threshold <= 255:
                break
            else:
                print("错误：阈值必须在 0 到 255 之间。")
        except ValueError:
            print("错误：输入无效，请输入一个整数。")

    return input_folder, output_folder, threshold

# --- 主程序入口 ---
if __name__ == "__main__":
    # 需要导入 shutil 用于复制文件
    import shutil

    print("欢迎使用图片黑边移除工具！")
    print("此工具会处理指定文件夹中的图片，尝试移除其黑色边框。")

    # 获取用户输入
    input_folder, output_folder, threshold = get_user_input_borders()

    # 显示用户输入的参数并请求确认
    print("\n请确认以下处理设置:")
    print(f"  [源文件夹]   : {input_folder}")
    print(f"  [目标文件夹] : {output_folder}")
    print(f"  [检测阈值]   : {threshold} (低于此值的像素视为黑边)")

    while True:
        confirm = input("是否根据以上设置开始处理? (y/n): ").lower().strip()
        if confirm == 'y':
            print("\n开始处理图片...")
            # 调用处理函数，传递用户输入的参数
            process_folder(input_folder, output_folder, threshold)
            break
        elif confirm == 'n':
            print("操作已取消。")
            sys.exit() # 退出脚本
        else:
            print("输入无效，请输入 'y' 或 'n'.")

    print("\n脚本执行完毕。")
    # input("按 Enter 键退出...") # 如果需要暂停