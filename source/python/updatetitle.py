import os
import re
from config import posts_path


import os
import re


def update_title_in_markdown(markdown_file):
    with open(markdown_file, 'r+') as f:
        content = f.read()
        pattern = r'^title:\s*(\S.*)?$'
        match = re.search(pattern, content, flags=re.MULTILINE)
        if not match:
            # 如果title后面没有字符串，则将文件名作为title的值
            filename = os.path.basename(markdown_file)
            new_content = re.sub(r'^title:\s*$', f'title: {filename}\n', content, flags=re.MULTILINE)
            f.seek(0)
            f.write(new_content)
            f.truncate()
            return True
        else:
            return False





def traverse_files(directory):
    # 遍历当前文件夹中的文件
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            update_title_in_markdown(file_path)
        elif os.path.isdir(file_path):
            # 递归遍历子文件夹
            traverse_files(file_path)


traverse_files(posts_path)