import argparse
from file_renamer import ItemRenamer

def main():
    parser = argparse.ArgumentParser(description='Mac 文件/文件夹批量重命名工具')
    parser.add_argument('directory', type=str, help='要处理的目录路径')
    parser.add_argument('--type', type=str, choices=['file', 'folder', 'both'], 
                      default='both', help='要处理的类型：file(文件)/folder(文件夹)/both(两者)')
    parser.add_argument('--prefix', type=str, default='', help='要添加的前缀')
    parser.add_argument('--suffix', type=str, default='', help='要添加的后缀')
    parser.add_argument('--pattern', type=str, default='', help='正则表达式模式')
    parser.add_argument('--replace-to', type=str, default='', help='替换成的文本')
    
    args = parser.parse_args()
    
    try:
        renamer = ItemRenamer(args.directory)
        results = renamer.rename_items(
            item_type=args.type,
            prefix=args.prefix,
            suffix=args.suffix,
            pattern=args.pattern,
            replace_to=args.replace_to
        )
        
        for result in results:
            if result['status'] == 'success':
                print(f"已重命名{result['type']}: {result['old_name']} -> {result['new_name']}")
            else:
                print(f"错误({result['type']}): {result['old_name']} -> {result['error']}")
                
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()
