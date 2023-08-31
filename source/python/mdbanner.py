import os
import random
from datetime import datetime

formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class MarkdownManipulator:
    def __init__(self, filename):
        self.filename = filename

    def add_title(self, image_folder):
        # 获取指定文件夹中的所有图片文件
        image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f)) and 'banne_photo' in f]

        # 随机选择一张图片作为new_index_img
        if image_files:
            new_index_img = random.choice(image_files)
        else:
            # 如果没有符合条件的图片，则使用默认值
            new_index_img = 'default.png'
            
        title = f'---\n\
title: \n\
date: {formatted_datetime}\n\
tags: []\n\
index_img: ../banner_images/{new_index_img}\n\
---\n'
        return title
        