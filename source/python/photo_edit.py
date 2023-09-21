import os
import re

def process_md_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    updated_lines = []

    for line in lines:
        match = re.search(r'!\[\]\(([^)]+\.(?:jpg|gif|png|jpeg|svg|webp))\)', line)
        if match:
            image_url = match.group(1)
            if not image_url.startswith('../images/'):
                updated_line = line.replace(match.group(), f'![](../images/{image_url})')
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(updated_lines)

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_md_file(file_path)

# 使用示例
target_directory = 'source/_posts'
process_directory(target_directory)