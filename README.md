# Mac 文件重命名工具

一个用于批量重命名文件和文件夹的命令行工具。

## 功能特点

- 支持同时处理文件和文件夹
- 可以选择只处理文件或只处理文件夹
- 支持添加前缀和后缀
- 支持正则表达式替换
- 保持文件扩展名不变

## 使用方法

基本命令格式：
python src/main.py [目录路径] [选项]

### 参数说明

- `directory`: 要处理的目录路径（必需）
- `--type`: 处理类型（可选，默认为 'both'）
  - `file`: 只处理文件
  - `folder`: 只处理文件夹
  - `both`: 同时处理文件和文件夹
- `--prefix`: 要添加的前缀（可选）
- `--suffix`: 要添加的后缀（可选）
- `--pattern`: 正则表达式模式（可选）
- `--replace-to`: 替换成的文本（可选）

### 使用示例

1. 只处理文件：
python src/main.py ~/Desktop/测试目录 --type file --prefix "新_" --suffix "_2024"

2. 只处理文件夹：
python src/main.py ~/Desktop/测试目录 --type folder --prefix "文件夹_" --suffix "_新"

3. 同时处理文件和文件夹：
python src/main.py ~/Desktop/测试目录 --type both --prefix "新_" --suffix "_2024"

4. 使用正则表达式替换：
python src/main.py ~/Desktop/测试目录 --pattern "旧.*文本" --replace-to "新文本"

## 注意事项

1. 使用前请备份重要文件和文件夹
2. 确保有足够的权限访问和修改目标目录
3. 文件名中避免使用特殊字符
4. 重命名操作不可撤销，请谨慎使用

## 开发环境

- Python 3.6+
- pathlib
