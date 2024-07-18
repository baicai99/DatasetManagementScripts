# DatasetManagementScripts

该项目提供了一个Python启动器脚本，通过该脚本用户可以选择运行不同的子脚本。

## 项目结构

```
DatasetManagementScripts/
├── add_prefix_to_txt_files.py
├── classify_images_by_orientation.py
├── delete_empty_txt_and_jpg.py
├── fractional_image_extractor.py
├── move_files.py
├── PhotoOptimizer.py
├── README.md
├── README.zh.md
├── run.py
└── split_files_into_folders.py
```

- `add_prefix_to_txt_files.py`：在所有txt文件的文件名前添加指定的前缀。

- `classify_images_by_orientation.py`：自动识别图片的方向（1:1、竖屏或横屏），并将图片分别移动到对应的文件夹中。

- `delete_empty_txt_and_jpg.py`：检查txt文件是否为空，如果为空，则同时删除该txt文件及其对应的jpg图片。

- `fractional_image_extractor.py`：从现有图片集中随机抽取一定比例（例如10%）的图片，用于创建验证集或测试集。

- `move_files.py`：根据指定规则移动文件到不同的目录。

- `PhotoOptimizer.py`：对图片进行批量优化处理，如去除白边等。

- `README.md`：英文版的README文件，提供脚本的基本信息和使用指南。

- `README.zh.md`：中文版的README文件，提供脚本的基本信息和使用指南。

- `run.py`：主执行脚本，通过此脚本可运行上述各个数据管理脚本。

- `split_files_into_folders.py`：将文件按照指定的规则分批划分到不同的文件夹中。

## 安装

1. 克隆该仓库到本地：
    ```bash
    git clone https://github.com/yourusername/DatasetManagementScripts.git
    cd DatasetManagementScripts
    ```

2. 确保你已安装Python环境。

## 使用方法

运行启动器脚本 `run.py`，并根据提示选择要运行的子脚本。

```bash
python run.py
```

启动脚本后，按照提示输入选项：

```
请选择要运行的脚本：
1. 在txt添加触发词，记得添加英文逗号。
2. 如果txt内容为空，则删除txt和对应的图片。
3. 随机提取10%图片放入新目录，正则化或者验证集可以使用。
4. 批量去白边
0. 退出
输入选项:
```

输入相应的数字后按回车键，即可运行对应的子脚本。

## 示例

假设你选择运行`add_prefix_to_txt_files.py`脚本：

```
输入选项: 1
```

系统将提示：

```
运行 add_prefix_to_txt_files.py ...
```

并执行该脚本。

## 注意事项

- 确保所有子脚本都放在与`launcher.py`相同的目录下。
- 如果出现文件未找到的错误，请检查脚本文件名和路径是否正确。

## 贡献

欢迎提交PR来改进本项目。如果你有任何建议或发现了问题，请创建Issue。

## 许可

该项目使用MIT许可。详情请参阅LICENSE文件。
```

这个README文件提供了项目概述、安装步骤、使用方法、示例、注意事项、贡献指南以及许可信息。你可以根据具体情况进一步修改和完善。