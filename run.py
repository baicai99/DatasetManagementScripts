import subprocess
import sys
import os

# 获取当前脚本的根目录（core目录）
# Get the current script's root directory (core directory)
script_directory = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
# Get the project root directory
project_root = os.path.dirname(script_directory)

def run_script(script_path):
    """
    运行指定路径的Python脚本
    Execute the Python script at the specified path
    
    参数 / Parameters:
        script_path: 脚本相对于项目根目录的路径
                    Relative path of the script from the project root
    """
    full_script_path = os.path.join(project_root, script_path)
    if not os.path.isfile(full_script_path):
        print(f"脚本文件 {script_path} 未找到，请检查路径。")
        print(f"Script file {script_path} not found. Please verify the path.")
        return
    
    try:
        print(f"\n正在运行 {os.path.basename(script_path)}...\n")
        print(f"\nExecuting {os.path.basename(script_path)}...\n")
        subprocess.run([sys.executable, full_script_path], check=True)
        print(f"\n{os.path.basename(script_path)} 执行完成\n")
        print(f"\n{os.path.basename(script_path)} execution completed\n")
    except subprocess.CalledProcessError as e:
        print(f"运行 {script_path} 时发生错误：{e}")
        print(f"Error occurred during execution of {script_path}: {e}")
    
    input("按Enter键返回主菜单... / Press Enter to return to the main menu...")

def main():
    print("\n===== 数据集管理工具集 / Dataset Management Toolkit =====\n")
    
    while True:
        print("\n请选择要运行的工具 / Please select a tool to execute:\n")
        print("\n文本文件处理工具 / Text File Processing Tools:")
        print("1. 添加触发词至TXT文件 / Add trigger words to TXT files")
        print("2. 删除空TXT文件及对应图片 / Remove empty TXT files and corresponding images")
        print("3. 追加字符至文件末尾 / Append characters to file end")
        print("4. 删除TXT文件中的指定字符串 / Remove specified strings from TXT files")
        print("5. 批量删除TXT文件 / Batch delete TXT files")
        
        print("\n文件管理工具 / File Management Tools:")
        print("6. 文件分组至多个文件夹 / Distribute files into multiple folders")
        print("7. 文件提升至父目录 / Move files to parent directory")
        print("8. 创建嵌套目录结构 / Create nested directory structure")
        print("9. 文件序列化重命名 / Sequential file renaming")
        
        print("\n图像处理工具 / Image Processing Tools:")
        print("10. 随机提取图像子集 / Extract random image subset")
        print("11. 批量去除白边 / Batch white border removal")
        print("12. 按方向分类图像 / Classify images by orientation")
        print("13. 图像中心裁剪 / Center crop images")
        print("14. 图像压缩至指定大小 / Compress images to specified size")
        print("15. 图像采样工具 / Image sampling utility")
        print("16. 移除图像黑边 / Remove black borders from images")
        print("17. 指定宽高比裁剪 / Aspect ratio-based cropping")
        
        print("\n视频处理工具 / Video Processing Tools:")
        print("18. 视频帧提取 / Video frame extraction")
        
        print("\n0. 退出 / Exit")
        
        choice = input("\n请输入选项编号 / Enter option number: ")
        
        # 文本文件处理工具 / Text File Processing Tools
        if choice == '1':
            run_script('text_utils/add_prefix_to_txt_files.py')
        elif choice == '2':
            run_script('text_utils/delete_empty_txt_and_jpg.py')
        elif choice == '3':
            run_script('text_utils/append_comma.py')
        elif choice == '4':
            run_script('text_utils/remove_string.py')
        elif choice == '5':
            run_script('text_utils/delete_txt_files.py')
        
        # 文件管理工具 / File Management Tools
        elif choice == '6':
            run_script('file_utils/split_files_into_folders.py')
        elif choice == '7':
            run_script('file_utils/move_files.py')
        elif choice == '8':
            run_script('file_utils/create_nested_folders.py')
        elif choice == '9':
            run_script('file_utils/sequential_file_renamer.py')
        
        # 图像处理工具 / Image Processing Tools
        elif choice == '10':
            run_script('image_utils/classification/fractional_image_extractor.py')
        elif choice == '11':
            run_script('image_utils/optimization/PhotoOptimizer.py')
        elif choice == '12':
            run_script('image_utils/classification/classify_images_by_orientation.py')
        elif choice == '13':
            run_script('image_utils/cropping/center_crop.py')
        elif choice == '14':
            run_script('image_utils/optimization/batch_image_compression.py')
        elif choice == '15':
            run_script('image_utils/sampling/image_sampler.py')
        elif choice == '16':
            run_script('image_utils/cropping/remove_black_borders.py')
        elif choice == '17':
            run_script('image_utils/cropping/aspect_ratio_cropper.py')
        
        # 视频处理工具 / Video Processing Tools
        elif choice == '18':
            run_script('video_utils/video_frame_extractor.py')
        
        elif choice == '0':
            print("程序已退出 / Program terminated")
            break
        else:
            print("无效选项，请重新选择 / Invalid option, please select again")

if __name__ == "__main__":
    main()