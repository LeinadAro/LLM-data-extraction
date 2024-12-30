import os
import sys
import shutil

#Copies files from a directory and renames files with sequential numerical names

try:
    root_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    counter = 1

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            
            new_name = f'{counter:04d}{os.path.splitext(file)[1]}'
            new_path = os.path.join(destination_dir, new_name)
            
            shutil.copy(file_path, new_path)
            
            counter += 1

    print("Copy and rename completed!")
    
except IndexError:
    print('Wrong arguments. There are 2 arguments: root_dir and destination_dir')