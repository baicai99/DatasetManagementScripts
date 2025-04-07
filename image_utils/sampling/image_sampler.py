import os
import shutil
import sys # 导入sys模块用于退出
# from pathlib import Path # pathlib在此脚本中未充分利用，暂时注释掉以简化

def sample_images(input_folder, output_folder, sample_rate=30):
    """
    从输入文件夹中每隔sample_rate张图片采样一张，保存到输出文件夹。
    按文件名中的数字（如果存在）进行排序后采样。

    参数:
        input_folder (str): 输入图片文件夹路径。
        output_folder (str): 输出图片文件夹路径。
        sample_rate (int): 采样率，必须 >= 1。
    """
    # --- 输入验证 ---
    if not os.path.isdir(input_folder):
        print(f"错误：输入文件夹不存在或不是一个有效的目录: {input_folder}")
        return

    if sample_rate < 1:
        print(f"错误：采样率 (sample_rate) 必须大于或等于 1。当前值为: {sample_rate}")
        return

    # --- 创建输出文件夹 ---
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"已创建输出文件夹: {output_folder}")
        # 可选：检查输出文件夹是否可写
        # if not os.access(output_folder, os.W_OK):
        #     print(f"错误：没有权限写入输出文件夹: {output_folder}")
        #     return
    except OSError as e:
        print(f"错误：无法创建或访问输出文件夹 {output_folder}。原因: {e}")
        return

    # --- 获取并排序图片文件 ---
    print("正在扫描输入文件夹并排序文件...")
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    image_files = []

    try:
        all_files = os.listdir(input_folder)
    except OSError as e:
        print(f"错误：无法读取输入文件夹内容 {input_folder}。原因: {e}")
        return

    for file in all_files:
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path):
            # 检查文件扩展名（不区分大小写）
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(file_path)

    if not image_files:
        print("错误：在输入文件夹中未找到任何支持的图片文件。")
        print(f"支持的扩展名: {', '.join(image_extensions)}")
        return

    # 按文件名中的数字排序（如果提取不到数字则视为0）
    # 注意：这种排序方式对于复杂的文件名可能不完美
    try:
        image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x) or '0')) or '0'))
        print(f"找到 {len(image_files)} 个图片文件，已排序。")
    except ValueError as e:
         print(f"警告：文件名排序时遇到问题 (可能存在非预期的字符导致无法转为整数): {e}。将尝试按原始字母顺序排序。")
         image_files.sort() # 出错时回退到简单排序

    # --- 采样并复制图片 ---
    print(f"开始采样，每隔 {sample_rate} 张复制一张...")
    sampled_count = 0
    copied_files = [] # 记录复制的文件名，避免重复复制（虽然理论上排序后不应重复）

    for i, img_path in enumerate(image_files):
        if i % sample_rate == 0:
            filename = os.path.basename(img_path)
            dest_path = os.path.join(output_folder, filename)

            # 避免因某种原因重复处理同一个文件
            if filename in copied_files:
                print(f"警告：检测到重复文件名，跳过: {filename}")
                continue

            try:
                shutil.copy2(img_path, dest_path) # copy2 保留元数据
                copied_files.append(filename)
                sampled_count += 1
                # 减少打印频率，可以每 N 张打印一次或使用 tqdm
                if sampled_count % 50 == 0 or sampled_count == 1: # 每50次或第一次打印
                    print(f"已复制 {sampled_count} 张: ... {filename}")
            except Exception as e: # 捕捉可能的复制错误 (权限、磁盘空间等)
                print(f"\n错误：复制文件 {filename} 到 {dest_path} 时失败。原因: {e}")
                # 可以选择在这里停止，或者继续处理下一个文件
                # break # 如果希望一出错就停止

    print(f"\n采样完成！")
    print(f"从总共 {len(image_files)} 张图片中，成功采样并复制了 {sampled_count} 张到:")
    print(f"{output_folder}")


def get_user_input_sampling():
    """获取用户输入的采样参数"""
    while True:
        input_folder = input("请输入包含图片的源文件夹路径: ").strip().strip('"').strip("'")
        if os.path.isdir(input_folder): # 检查是否是目录
            break
        else:
            print("错误：输入的路径不存在或不是一个有效的文件夹，请重新输入。")

    while True:
        output_folder = input("请输入保存采样图片的目标文件夹路径: ").strip().strip('"').strip("'")
        if output_folder: # 确保非空
             # 允许输入不存在的路径，脚本会自动创建
             if os.path.exists(output_folder) and not os.path.isdir(output_folder):
                 print(f"错误：输出路径 '{output_folder}' 已存在但不是一个文件夹，请选择其他路径或删除该文件。")
             elif os.path.exists(output_folder) and os.listdir(output_folder):
                 confirm_overwrite = input(f"警告：输出文件夹 '{output_folder}' 已存在且非空，继续操作可能会覆盖同名文件。是否继续? (y/n): ").lower().strip()
                 if confirm_overwrite == 'y':
                     break
                 else:
                     print("操作已取消，请选择新的输出文件夹。")
             else: # 路径不存在或者是空文件夹
                 break
        else:
             print("错误：输出文件夹路径不能为空，请重新输入。")

    while True:
        try:
            sample_rate_str = input("请输入采样率 (每隔 N 张采样一张，输入正整数，默认为 30): ").strip()
            if not sample_rate_str: # 用户直接回车，使用默认值
                sample_rate = 30
            else:
                sample_rate = int(sample_rate_str)
            if sample_rate >= 1:
                break
            else:
                print("错误：请输入一个大于或等于 1 的整数。")
        except ValueError:
            print("错误：输入无效，请输入一个整数。")

    return input_folder, output_folder, sample_rate

if __name__ == "__main__":
    print("欢迎使用图片采样工具！")
    print("此工具会从源文件夹中按文件名排序后，每隔指定数量复制一张图片到目标文件夹。")

    # 获取用户输入
    input_folder, output_folder, sample_rate = get_user_input_sampling()

    # 显示用户输入的参数并请求确认
    print("\n请确认以下采样设置:")
    print(f"  [源文件夹]   : {input_folder}")
    print(f"  [目标文件夹] : {output_folder}")
    print(f"  [采样间隔]   : 每 {sample_rate} 张图片采样一张")

    while True:
        confirm = input("是否根据以上设置开始采样? (y/n): ").lower().strip()
        if confirm == 'y':
            print("\n开始处理...")
            # 调用采样函数
            sample_images(input_folder, output_folder, sample_rate)
            break
        elif confirm == 'n':
            print("操作已取消。")
            sys.exit() # 退出脚本
        else:
            print("输入无效，请输入 'y' 或 'n'.")

    print("\n脚本执行完毕。")
    # 可以在这里加一个 input("按 Enter 键退出...") 如果不希望窗口立刻关闭