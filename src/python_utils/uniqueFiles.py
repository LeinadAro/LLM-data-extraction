import os
import sys
import shutil
import hashlib

#Copies files from a directory checking for duplicated content. Duplicates are discarded.
#The files in the new directory are renamed with sequential numbers.

def get_file_hash(file_path):
    hash_sha256 = hashlib.sha256()  # Create a SHA256 hash object
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read the file in chunks
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

try:
    root_dir = sys.argv[1]  
    destination_dir = sys.argv[2]
    if os.path.isdir(root_dir):
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        file_hashes = set()

        counter = 1

        for subdir, dirs, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(subdir, file)

                file_hash = get_file_hash(file_path)

                if file_hash not in file_hashes:
                    file_hashes.add(file_hash)
                    
                    new_name = f'{counter:04d}{os.path.splitext(file)[1]}'
                    new_path = os.path.join(destination_dir, new_name)
                    
                    shutil.copy(file_path, new_path)
                    
                    counter += 1

        print("Unique files copied and renamed successfully!")
    else:
        print(f'{root_dir} does not exist')
except IndexError:
    print('Wrong arguments. There are 2: directory with duplicates, new directory')