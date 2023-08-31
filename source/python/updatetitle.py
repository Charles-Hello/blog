import os
import re
from config import posts_path



def update_title_in_markdown(markdown_file):
    with open(markdown_file, 'r+', encoding='utf-8') as f:
        content = f.read()
        filename = os.path.basename(markdown_file)
        filename = os.path.splitext(filename)[0]
        new_content = re.sub(r'^(---\n)title.*', fr'\1title: {filename}', content)
        f.seek(0)
        f.write(new_content)
        f.truncate()
        return True




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