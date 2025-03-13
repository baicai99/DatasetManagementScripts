# 数据集管理脚本

这个项目提供了一个 Python 启动器脚本，允许用户选择和运行不同的子脚本。

## 项目结构

```
DatasetManagementScripts/
├── add_prefix_to_txt_files.py
├── append_comma.py
├── batch_image_compression.py
├── center_crop.py
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

- `add_prefix_to_txt_files.py`：为所有 txt 文件的文件名添加指定前缀。
- `append_comma.py`：在 txt 文件的每行末尾添加逗号。
- `batch_image_compression.py`：将图片压缩到指定的 KB 大小。
- `center_crop.py`：裁剪图片的中心部分。
- `classify_images_by_orientation.py`：自动识别图片方向（1:1、竖向或横向）并移动到相应文件夹。
- `delete_empty_txt_and_jpg.py`：检查 txt 文件是否为空，删除空的 txt 文件及其对应的 jpg 图片。
- `fractional_image_extractor.py`：从现有数据集中随机提取一定比例（如 10%）的图片，用于创建验证集或测试集。
- `move_files.py`：根据指定规则将文件移动到不同目录。
- `PhotoOptimizer.py`：批量优化图片，如去除白边。
- `README.md`：英文版说明文件，提供脚本的基本信息和使用指南。
- `README.zh.md`：中文版说明文件，提供脚本的基本信息和使用指南。
- `run.py`：主执行脚本，允许运行各种数据管理脚本。
- `split_files_into_folders.py`：根据指定规则将文件分割到不同文件夹。
- `remove_string.py`:删除txt文件中的指定字符串。

## 安装

1. 将仓库克隆到本地：
    ```bash
    git clone https://github.com/yourusername/DatasetManagementScripts.git
    cd DatasetManagementScripts
    ```

2. 确保安装了 Python 环境。

## 使用方法

运行启动器脚本 `run.py`，根据提示选择要执行的子脚本。

```bash
python run.py
```

启动脚本后，按照提示选择选项：

```
请选择要运行的脚本：
1. 为 txt 文件添加前缀
2. 删除空的 txt 和对应的图片
3. 随机提取 10% 的图片到新目录（如用于验证集或测试集）
4. 批量去除白边
5. 将文件分割到文件夹
6. 按方向分类图片
7. 将文件移动到父目录
8. 为 txt 文件添加逗号
9. 中心裁剪图片
10. 将图片压缩到指定 KB
0. 退出
请输入选项：
```

输入相应数字并按 Enter 键运行所选子脚本。

## 示例

假设您选择运行 `add_prefix_to_txt_files.py` 脚本：

```
请输入选项：1
```

系统将提示：

```
正在运行 add_prefix_to_txt_files.py ...
```

并执行脚本。

## 注意事项

- 确保所有子脚本都在与 `run.py` 相同的目录中。
- 如果遇到文件未找到错误，请检查脚本文件名和路径。

## 贡献

欢迎贡献。请提交 PR 来改进这个项目。如果您有任何建议或发现任何问题，请创建 Issue。

## 许可证

本项目采用 MIT 许可证。有关详细信息，请参阅 LICENSE 文件。

---

本 README 文件提供了项目概述、安装步骤、使用说明、示例、注意事项、贡献指南和许可信息。请根据您的具体需求修改和完善。