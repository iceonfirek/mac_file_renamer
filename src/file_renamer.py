import os
import re
from pathlib import Path

class ItemRenamer:
    def __init__(self, base_directory: str):
        self.base_directory = Path(base_directory)
        if not self.base_directory.exists():
            raise FileNotFoundError(f"目录不存在：{base_directory}")
    
    def rename_items(self, 
                    item_type: str = 'both',
                    prefix: str = '',
                    suffix: str = '',
                    pattern: str = '',
                    replace_to: str = '') -> list:
        """
        批量重命名文件或文件夹
        
        Args:
            item_type: 要处理的类型 ('file'=文件, 'folder'=文件夹, 'both'=两者都处理)
            prefix: 要添加的前缀
            suffix: 要添加的后缀
            pattern: 正则表达式模式
            replace_to: 替换成的文本
        """
        results = []
        
        try:
            for item_path in self.base_directory.iterdir():
                # 根据类型过滤
                if item_type == 'file' and not item_path.is_file():
                    continue
                if item_type == 'folder' and not item_path.is_dir():
                    continue
                
                # 获取原名称
                original_name = item_path.name
                
                # 处理文件名
                if item_path.is_file():
                    stem = item_path.stem
                    suffix_orig = item_path.suffix
                    new_name = stem
                else:
                    new_name = original_name
                    suffix_orig = ''
                
                # 应用正则替换
                if pattern:
                    new_name = re.sub(pattern, replace_to, new_name)
                
                # 添加前缀和后缀
                new_name = f"{prefix}{new_name}{suffix}{suffix_orig}"
                
                # 构建新路径并重命名
                new_path = item_path.parent / new_name
                item_path.rename(new_path)
                
                item_type_str = "文件夹" if item_path.is_dir() else "文件"
                results.append({
                    'type': item_type_str,
                    'old_name': original_name,
                    'new_name': new_name,
                    'status': 'success'
                })
                    
        except Exception as e:
            results.append({
                'type': item_type_str,
                'old_name': original_name,
                'new_name': new_name,
                'status': 'error',
                'error': str(e)
            })
            
        return results
