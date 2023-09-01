import os
import shutil

def move_images_to_images_folder(directory_path):
    images_folder = "source/images"
    
    if not os.path.exists(images_folder):
        os.mkdir(images_folder)
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.png', '.jpeg', '.svg', '.webp')):
                file_path = os.path.join(root, file)
                new_file_path = os.path.join(images_folder, file)
                shutil.move(file_path, new_file_path)
                print(f"Moved '{file}' to 'images' folder.")
    
# 使用示例
target_directory = 'source/_posts'
move_images_to_images_folder(target_directory)