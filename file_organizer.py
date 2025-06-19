import os
import shutil
from pathlib import Path

def organize_files(folder_path):
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar'],
        'Scripts': ['.py', '.js', '.html', '.css']
    }

    files = os.listdir(folder_path)
    print(f"Organizing {len(files)} files in: {folder_path}")

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = Path(file).suffix.lower()
            moved = False
            for folder, ext_list in extensions.items():
                if ext in ext_list:
                    target_dir = os.path.join(folder_path, folder)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, file))
                    print(f"Moved '{file}' to '{folder}'")
                    moved = True
                    break
            if not moved:
                other_dir = os.path.join(folder_path, 'Others')
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(other_dir, file))
                print(f"Moved '{file}' to 'Others'")

# Input folder
user_folder = input("Enter the full folder path you want to organize (e.g., C:/Users/XYZ/Downloads): ")
if os.path.exists(user_folder):
    organize_files(user_folder)
else:
    print("Invalid folder path. Please check and try again.")