import os
import shutil
import random

def get_user_input(default_value):
    user_input = input(f"请输入占比（例如 0.7），回车则使用默认值 {default_value}: ")
    return float(user_input) if user_input else default_value

def split_dataset(src_dir, train_ratio=0.7, test_ratio=0.2, val_ratio=0.1):
    # 获取源目录中的所有文件
    files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
    
    # 确保比例和文件数量合理
    if train_ratio + test_ratio + val_ratio != 1.0:
        print("占比和不等于 1.0，请重新输入。")
        return
    
    # 随机打乱文件
    random.shuffle(files)
    
    # 计算各集的文件数量
    total_files = len(files)
    train_size = int(train_ratio * total_files)
    test_size = int(test_ratio * total_files)
    val_size = total_files - train_size - test_size  # 剩下的为验证集
    
    # 划分数据集
    train_files = files[:train_size]
    test_files = files[train_size:train_size + test_size]
    val_files = files[train_size + test_size:]
    
    # 创建目录
    os.makedirs(os.path.join(src_dir, 'train'), exist_ok=True)
    os.makedirs(os.path.join(src_dir, 'test'), exist_ok=True)
    os.makedirs(os.path.join(src_dir, 'val'), exist_ok=True)

    # 迁移文件
    for file in train_files:
        shutil.move(os.path.join(src_dir, file), os.path.join(src_dir, 'train', file))
        move_caption_file(src_dir, file, 'train')
    
    for file in test_files:
        shutil.move(os.path.join(src_dir, file), os.path.join(src_dir, 'test', file))
        move_caption_file(src_dir, file, 'test')
    
    for file in val_files:
        shutil.move(os.path.join(src_dir, file), os.path.join(src_dir, 'val', file))
        move_caption_file(src_dir, file, 'val')
    
    print(f"数据集划分完成：训练集: {len(train_files)}，测试集: {len(test_files)}，验证集: {len(val_files)}")

def move_caption_file(src_dir, file_name, target_dir):
    caption_file = file_name.rsplit('.', 1)[0] + '.txt'  # 假设 caption 文件是 .txt 格式
    caption_path = os.path.join(src_dir, caption_file)
    
    if os.path.exists(caption_path):
        shutil.move(caption_path, os.path.join(src_dir, target_dir, caption_file))

if __name__ == "__main__":
    # 获取用户输入的比例
    train_ratio = get_user_input(0.7)
    test_ratio = get_user_input(0.2)
    val_ratio = get_user_input(0.1)
    
    # 获取数据集目录
    src_dir = input("请输入数据集所在目录路径: ")
    
    # 确认数据集目录是否存在
    if not os.path.exists(src_dir):
        print(f"目录 {src_dir} 不存在，请检查路径。")
    else:
        split_dataset(src_dir, train_ratio, test_ratio, val_ratio)
