import os

# 从终端获取路径输入
base_path = input("请输入基路径：")

# 月份列表
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

# 第一层：创建12个月份文件夹
for month in months:
    folder_1 = os.path.join(base_path, month)
    os.makedirs(folder_1, exist_ok=True)
    
    # 第二层：在每个月份文件夹中创建10个子文件夹
    for j in range(10):
        folder_2 = os.path.join(folder_1, f"subfolder_{j+1}")
        os.makedirs(folder_2, exist_ok=True)
        
        # 第三层：在每个子文件夹中再创建10个文件夹
        for k in range(10):
            folder_3 = os.path.join(folder_2, f"subsubfolder_{k+1}")
            os.makedirs(folder_3, exist_ok=True)

print("文件夹创建完成！")