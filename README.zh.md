# DatasetManagementScripts

该项目提供了一个Python启动器脚本，通过该脚本用户可以选择运行不同的子脚本。

## 项目结构

```
DatasetManagementScripts/
│
├── add_prefix_to_txt_files.py
├── delete_empty_txt_and_jpg.py
├── extract_and_cleanup_images.py
├── PhotoOptimizer.py
└── run.py
```

- `add_prefix_to_txt_files.py`：在txt文件中添加触发词，记得添加英文逗号。
- `delete_empty_txt_and_jpg.py`：如果txt文件内容为空，则删除txt文件和对应的图片。
- `extract_and_cleanup_images.py`：随机提取10%的图片放入新目录，正则化或者验证集可以使用。
- `PhotoOptimizer.py`：批量去除图片白边。
- `launcher.py`：启动器脚本，可以通过此脚本选择运行上述子脚本。

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