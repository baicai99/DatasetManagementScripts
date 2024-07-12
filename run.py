import subprocess
import sys
import os

# 获取当前脚本的根目录
script_directory = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    script_path = os.path.join(script_directory, script_name)
    if not os.path.isfile(script_path):
        print(f"脚本文件 {script_name} 未找到，请检查路径。")
        return
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"运行 {script_name} 时发生错误：{e}")

def main():
    while True:
        print("请选择要运行的脚本：")
        print("1. 在txt添加触发词，记得添加英文逗号。")
        print("2. 如果txt内容为空，则删除txt和对应的图片。")
        print("3. 随机提取10%图片放入新目录，正则化或者验证集可以使用。")
        print("4. 批量去白边")
        print("5. 拆分文件夹")
        print("6. 提取所有文件到文件夹")
        print("7. 2/3图片提取到reg文件夹")
        print("8. 把图片分为横屏、竖屏、正方形")
        print("0. 退出")
        
        choice = input("输入选项: ")
        
        if choice == '1':
            run_script('add_prefix_to_txt_files.py')
        elif choice == '2':
            run_script('delete_empty_txt_and_jpg.py')
        elif choice == '3':
            run_script('extract_and_cleanup_images.py')
        elif choice == '4':
            run_script('PhotoOptimizer.py')
        elif choice == '5':
            run_script('split_files_into_folders.py')
        elif choice == '6':            
            run_script('extract_all_files.py')
        elif choice == '7':
            run_script('extract_two_thirds_files.py')
        elif choice == '8':
             run_script('classify_images_by_orientation.py')
        elif choice == '0':
            print("退出程序")
            break
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    main()
