import os

filename = '未命名.md'
content_to_add = '1111'

# 获取当前文件夹路径
current_directory = os.getcwd()+"\source\python"

# 遍历当前文件夹中的文件
for file in os.listdir(current_directory):
    if file == filename:
        # 找到目标文件
        file_path = os.path.join(current_directory, file)
        with open(file_path, 'r+', encoding='utf-8') as f:
            f.write(content_to_add)
