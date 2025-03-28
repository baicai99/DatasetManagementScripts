# 给视频截取帧数

import cv2
import os
import concurrent.futures
import numpy as np
from tqdm import tqdm

def save_frame(frame_data):
    frame, frame_path = frame_data
    cv2.imwrite(frame_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
    return True

def extract_frames(video_path, output_folder, skip_frames=1, num_workers=8):
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    
    # 检查视频是否成功打开
    if not video.isOpened():
        print("错误：无法打开视频文件！")
        return
    
    # 获取视频的总帧数和FPS
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    print(f"视频总帧数: {total_frames}, FPS: {fps}")
    
    # 计算实际要处理的帧数
    frames_to_process = total_frames // skip_frames
    print(f"将提取 {frames_to_process} 帧 (每 {skip_frames} 帧提取一帧)")
    
    # 准备并行处理
    frame_data = []
    count = 0
    
    # 使用tqdm创建进度条
    with tqdm(total=frames_to_process, desc="读取帧") as pbar:
        while count < total_frames:
            success, frame = video.read()
            if not success:
                break
                
            if count % skip_frames == 0:
                frame_filename = os.path.join(output_folder, f"frame_{count//skip_frames:06d}.jpg")
                frame_data.append((frame.copy(), frame_filename))
                pbar.update(1)
                
            count += 1
            
            # 每积累一定数量的帧，就进行批处理以节省内存
            if len(frame_data) >= 100:
                with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
                    list(executor.map(save_frame, frame_data))
                frame_data = []
    
    # 处理剩余的帧
    if frame_data:
        print("处理剩余帧...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            list(executor.map(save_frame, frame_data))
    
    # 释放视频资源
    video.release()
    print(f"完成！已提取 {len(frame_data)} 帧到 {output_folder}")

if __name__ == "__main__":
    # 修改这些路径和参数
    video_path = r"D:\\BaiduNetdiskDownload\\Arcane\\S02E02.mkv"
    output_folder = r"C:\\Users\\Administrator\\Desktop\\Arcane\\S02E02"
    
    # 每隔多少帧提取一帧 (1=所有帧, 2=每两帧提取一帧)
    skip_frames = 1  
    
    # 并行工作线程数
    num_workers = 8   # 根据CPU核心数调整
    
    extract_frames(video_path, output_folder, skip_frames, num_workers)