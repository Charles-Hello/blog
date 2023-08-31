import os
from mdbanner import MarkdownManipulator
from config import posts_path, photo_path


filename = '未命名.md'
markdown_manipulator = MarkdownManipulator(filename)
content_to_add = markdown_manipulator.add_title(photo_path)



def traverse_files(directory):
    # 遍历当前文件夹中的文件
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file == filename:
            # 找到目标文件
            with open(file_path, 'r+', encoding='utf-8') as f:
                f.seek(0, 0)  # 将文件指针移到文件开头
                f.write(content_to_add + '\n')
        elif os.path.isdir(file_path):
            # 递归遍历子文件夹
            traverse_files(file_path)


traverse_files(posts_path)

