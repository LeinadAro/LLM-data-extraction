import os
import shutil
import hashlib

# Function to compute file hash
def get_file_hash(file_path):
    hash_sha256 = hashlib.sha256()  # Create a SHA256 hash object
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read the file in chunks
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

# Directories
root_dir = r'C:\Users\Garda6\raw-data'  # Directory to scan for files
destination_dir = r'C:\Users\Garda6\unique-data'  # Directory where unique files will be copied

# Create destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Set to track the hashes of files we've already encountered
file_hashes = set()

# Counter for renaming the files sequentially
counter = 1

# Walk through the directory and subdirectories
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(subdir, file)

        # Compute the file's hash (content-based)
        file_hash = get_file_hash(file_path)

        # If the file's content hasn't been encountered before, it's unique
        if file_hash not in file_hashes:
            # Add the hash to the set to track it
            file_hashes.add(file_hash)
            
            # Create a new sequential name for the file
            new_name = f'{counter:04d}{os.path.splitext(file)[1]}'
            new_path = os.path.join(destination_dir, new_name)
            
            # Copy the file to the destination with the new name
            shutil.copy(file_path, new_path)
            
            # Increment the counter for the next file
            counter += 1

print("Unique files copied and renamed successfully!")
