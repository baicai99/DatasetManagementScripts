# 给视频截取帧数

import cv2
import os
import concurrent.futures
import numpy as np
from tqdm import tqdm
import sys # 导入sys模块用于退出

def save_frame(frame_data):
    """将单个帧保存到文件"""
    frame, frame_path = frame_data
    # 使用JPEG格式保存，质量为95（可以调整）
    cv2.imwrite(frame_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
    return True

def extract_frames(video_path, output_folder, skip_frames=1, num_workers=8):
    """
    从视频文件中提取帧并保存为图像。

    参数:
        video_path (str): 输入视频文件的路径。
        output_folder (str): 保存提取帧的文件夹路径。
        skip_frames (int): 每隔多少帧提取一帧 (1=所有帧, 2=每两帧提取一帧, ...)。
        num_workers (int): 用于并行保存帧的工作线程数。
    """
    # 检查输入路径是否存在
    if not os.path.exists(video_path):
        print(f"错误：视频文件不存在！路径：{video_path}")
        return
    if not os.path.isfile(video_path):
         print(f"错误：提供的输入路径不是一个文件！路径：{video_path}")
         return

    # 创建输出文件夹（如果不存在）
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"已创建输出文件夹: {output_folder}")
    except OSError as e:
        print(f"错误：无法创建输出文件夹 {output_folder}。原因: {e}")
        return

    # 打开视频文件
    video = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not video.isOpened():
        print(f"错误：无法打开视频文件！路径：{video_path}")
        return

    # 获取视频的总帧数和FPS
    try:
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = video.get(cv2.CAP_PROP_FPS)
        if total_frames <= 0:
            print("警告：无法获取视频总帧数，或视频为空。")
            # 可以在这里选择退出或尝试继续，但可能会出错
            # return
        print(f"视频总帧数: {total_frames}, FPS: {fps:.2f}")
    except Exception as e:
        print(f"错误：获取视频信息时出错。原因: {e}")
        video.release()
        return

    # 计算实际要处理的帧数
    if skip_frames < 1:
        print("警告：skip_frames 值必须大于等于 1，将使用默认值 1。")
        skip_frames = 1
    frames_to_process = total_frames // skip_frames if total_frames > 0 else 0
    if frames_to_process == 0 and total_frames > 0 :
         print(f"警告：skip_frames ({skip_frames}) 大于总帧数 ({total_frames})，不会提取任何帧。")
         # return # 根据需要决定是否在这里退出

    print(f"将提取大约 {frames_to_process} 帧 (每 {skip_frames} 帧提取一帧)")

    # --- 开始处理 ---
    print("\n开始读取和处理帧...")

    frame_data_buffer = [] # 用于批量处理的缓冲区
    processed_frame_count = 0
    frame_read_count = 0

    # 使用tqdm创建进度条，基于预计处理的帧数
    with tqdm(total=frames_to_process, desc="处理帧", unit="帧") as pbar:
        while True:
            success, frame = video.read()
            if not success:
                print("\n已到达视频末尾或读取帧失败。")
                break # 读取结束或失败

            # 检查是否需要处理当前帧
            if frame_read_count % skip_frames == 0:
                # 生成文件名 (使用处理后的帧计数，保证序号连续)
                frame_filename = os.path.join(output_folder, f"frame_{processed_frame_count:06d}.jpg")
                # 将帧的副本和路径添加到缓冲区
                frame_data_buffer.append((frame.copy(), frame_filename))
                processed_frame_count += 1
                pbar.update(1) # 更新进度条

            frame_read_count += 1

            # 每积累一定数量的帧（例如100帧）或处理完所有帧时，进行批处理保存以平衡内存使用
            # 调整 buffer_size 可以影响内存占用和写入频率
            buffer_size = num_workers * 10 # 稍微增大缓冲区，减少线程池启动次数
            if len(frame_data_buffer) >= buffer_size:
                try:
                    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
                        # map会阻塞直到所有任务完成
                        list(executor.map(save_frame, frame_data_buffer))
                except Exception as e:
                    print(f"\n保存帧时发生错误: {e}")
                    # 可以考虑更详细的错误处理，比如记录失败的帧
                frame_data_buffer = [] # 清空缓冲区

    # 处理缓冲区中剩余的最后一批帧
    if frame_data_buffer:
        print("\n处理剩余的帧...")
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
                list(executor.map(save_frame, frame_data_buffer))
        except Exception as e:
            print(f"\n保存剩余帧时发生错误: {e}")
        remaining_count = len(frame_data_buffer)
        print(f"已处理完剩余 {remaining_count} 帧。")

    # 释放视频资源
    video.release()
    print(f"\n完成！总共提取并保存了 {processed_frame_count} 帧到文件夹: {output_folder}")

def get_user_input():
    """获取用户输入的参数"""
    while True:
        video_path = input("请输入视频文件的完整路径: ").strip().strip('"').strip("'") # 去除首尾空格和可能的引号
        if os.path.exists(video_path) and os.path.isfile(video_path):
            break
        else:
            print("错误：输入的路径不存在或不是一个文件，请重新输入。")

    while True:
        output_folder = input("请输入保存帧的输出文件夹路径: ").strip().strip('"').strip("'")
        # 允许用户输入一个不存在的路径，程序会自动创建
        # 可以添加检查，例如检查路径是否有效或是否有写入权限（更复杂）
        if output_folder: # 确保输入不为空
             break
        else:
             print("错误：输出文件夹路径不能为空，请重新输入。")


    while True:
        try:
            skip_frames_str = input("每隔多少帧提取一帧? (输入整数, 1=所有帧, 默认为 1): ").strip()
            if not skip_frames_str: # 用户直接回车，使用默认值
                skip_frames = 1
            else:
                skip_frames = int(skip_frames_str)
            if skip_frames >= 1:
                break
            else:
                print("错误：请输入一个大于或等于1的整数。")
        except ValueError:
            print("错误：输入无效，请输入一个整数。")

    default_workers = os.cpu_count() or 4 # 获取CPU核心数作为默认值，如果失败则用4
    while True:
        try:
            num_workers_str = input(f"使用多少个线程处理? (输入整数, 推荐 <= {default_workers}, 默认为 {default_workers}): ").strip()
            if not num_workers_str: # 用户直接回车，使用默认值
                num_workers = default_workers
            else:
                num_workers = int(num_workers_str)
            if num_workers >= 1:
                break
            else:
                print("错误：请输入一个大于或等于1的整数。")
        except ValueError:
            print("错误：输入无效，请输入一个整数。")

    return video_path, output_folder, skip_frames, num_workers

if __name__ == "__main__":
    print("欢迎使用视频帧提取工具！")

    # 获取用户输入
    video_path, output_folder, skip_frames, num_workers = get_user_input()

    # 显示用户输入的参数并请求确认
    print("\n请确认以下信息:")
    print(f"  视频文件: {video_path}")
    print(f"  输出目录: {output_folder}")
    print(f"  提取间隔: 每 {skip_frames} 帧提取一帧")
    print(f"  处理线程数: {num_workers}")

    while True:
        confirm = input("是否开始处理? (y/n): ").lower().strip()
        if confirm == 'y':
            # 开始提取帧
            extract_frames(video_path, output_folder, skip_frames, num_workers)
            break
        elif confirm == 'n':
            print("操作已取消。")
            sys.exit() # 退出脚本
        else:
            print("输入无效，请输入 'y' 或 'n'.")