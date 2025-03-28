# 数据集管理工具集

这个项目提供了一套用于管理和处理数据集的Python工具集，特别适合于机器学习数据集的预处理、组织和优化。

## 项目结构

```
project_root/
├── core/
│   └── run.py                             # 主菜单程序
│
├── file_utils/
│   ├── create_nested_folders.py           # 创建嵌套文件夹
│   ├── move_files.py                      # 移动文件到父文件夹
│   ├── sequential_file_renamer.py         # 顺序重命名文件
│   └── split_files_into_folders.py        # 拆分文件到多个文件夹
│
├── image_utils/
│   ├── classification/
│   │   ├── classify_images_by_orientation.py  # 按横竖屏分类图片
│   │   └── fractional_image_extractor.py      # 随机提取一部分图片
│   │
│   ├── cropping/
│   │   ├── aspect_ratio_cropper.py        # 按特定宽高比裁剪
│   │   ├── center_crop.py                 # 中心裁剪
│   │   └── remove_black_borders.py        # 移除图像黑边
│   │
│   ├── optimization/
│   │   ├── batch_image_compression.py     # 压缩图片到指定大小
│   │   └── PhotoOptimizer.py              # 批量去白边优化
│   │
│   └── sampling/
│       └── image_sampler.py               # 图像采样器
│
├── text_utils/
│   ├── add_prefix_to_txt_files.py         # 在txt添加触发词
│   ├── append_comma.py                    # 末尾追加任意字符
│   ├── delete_empty_txt_and_jpg.py        # 删除空txt和对应图片
│   ├── delete_txt_files.py                # 删除所有txt文件
│   └── remove_string.py                   # 删除txt中的指定字符串
│
├── video_utils/
│   └── video_frame_extractor.py           # 从视频提取帧
│
└── docs/
    ├── LICENSE                            # 许可证文件
    ├── README.md                          # 英文说明文档
    └── README.zh.md                       # 中文说明文档
```

## 工具说明

### 文本文件处理工具

- `add_prefix_to_txt_files.py`：为txt文件添加前缀或触发词，支持添加英文逗号分隔的多个词
- `append_comma.py`：在txt文件内容末尾追加任意指定字符
- `delete_empty_txt_and_jpg.py`：检查并删除内容为空的txt文件及其对应同名的图片文件
- `delete_txt_files.py`：批量删除指定目录下的所有txt文件
- `remove_string.py`：从txt文件中删除指定的字符串或短语

### 文件管理工具

- `create_nested_folders.py`：按照指定结构创建嵌套的文件夹层次
- `move_files.py`：将文件从子文件夹移动到父文件夹，方便集中管理
- `sequential_file_renamer.py`：按顺序重命名文件，保持统一的命名格式
- `split_files_into_folders.py`：将大量文件按照指定数量分割到多个子文件夹中

### 图像处理工具

#### 分类工具
- `classify_images_by_orientation.py`：自动识别图片方向（横屏、竖屏、正方形）并分类到不同文件夹
- `fractional_image_extractor.py`：随机提取一定比例（如10%）的图片到新目录，用于创建验证集或测试集

#### 裁剪工具
- `center_crop.py`：对图片进行中心裁剪，保留中心区域
- `aspect_ratio_cropper.py`：将图片裁剪成特定的宽高比
- `remove_black_borders.py`：自动检测并移除图片周围的黑色边框

#### 优化工具
- `batch_image_compression.py`：批量压缩图片到指定的KB大小，节省存储空间
- `PhotoOptimizer.py`：批量优化图片，包括去除白边等功能

#### 采样工具
- `image_sampler.py`：从图像数据集中智能采样，用于数据分析或创建子集

### 视频处理工具

- `video_frame_extractor.py`：从视频文件中按指定间隔提取帧，生成图像序列

## 安装

1. 克隆仓库到本地：
    ```bash
    git clone https://github.com/yourusername/dataset-management-tools.git
    cd dataset-management-tools
    ```

2. 确保已安装Python环境和所需依赖库：
    ```bash
    pip install -r requirements.txt
    ```

## 使用方法

运行主菜单程序，通过交互式界面选择要执行的工具：

```bash
python core/run.py
```

程序会显示分类菜单，根据提示选择相应的工具：

```
===== 图像处理工具集 =====

请选择要运行的脚本：

文本文件处理工具:
1. 在txt添加触发词，记得添加英文逗号。
2. 如果txt内容为空，则删除txt和对应的图片。
3. 末尾追加任意字符
4. 删除txt文件中的指定字符串
5. 删除txt文件

文件管理工具:
6. 拆分文件夹
7. 把图片移动到父文件夹
8. 创建嵌套文件夹
9. 文件序列化重命名

图像处理工具:
10. 随机提取10%图片放入新目录，正则化或者验证集可以使用。
11. 批量去白边
12. 把图片分为横屏、竖屏、正方形
13. 中心裁剪
14. 压缩图片到指定kb
15. 图像采样器
16. 移除图像黑边
17. 图像宽高比裁剪

视频处理工具:
18. 从视频提取帧

0. 退出

输入选项: 
```

## 注意事项

- 在运行工具前，请确保已备份重要数据，某些工具会执行不可逆的文件操作
- 所有脚本运行前都会提示确认，以防误操作
- 如遇到路径问题，请检查文件夹结构是否与预期一致

## 贡献

欢迎贡献新工具或改进现有工具。请提交PR或创建Issue来讨论新功能或报告问题。

## 许可证

本项目采用MIT许可证。有关详细信息，请参阅LICENSE文件。