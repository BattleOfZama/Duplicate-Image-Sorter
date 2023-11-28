import os
import shutil
from itertools import count

def unique_file(destination, filename):
    """
    Generate a unique filename by appending a count if a file with the same name exists.
    """
    base, extension = os.path.splitext(filename)
    for i in count(1):
        unique_name = f"{base}_{i}{extension}"
        if not os.path.exists(os.path.join(destination, unique_name)):
            return unique_name

def move_files_in_batches(src_dir, dst_dir, file_types, log_file_path, batch_size=100):
    """
    Move files of specified types from src_dir to dst_dir in batches.
    Log details including file types detected, number of folders, and number of files.
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    total_files_moved = 0
    file_count = 0
    folder_count = 0
    file_types_detected = set()

    with open(log_file_path, 'w') as log_file:
        for root, dirs, files in os.walk(src_dir):
            folder_count += 1
            for file in files:
                if file.endswith(tuple(file_types)):
                    file_count += 1
                    file_types_detected.add(os.path.splitext(file)[1].lower())

                    if file_count % batch_size == 0:
                        log_file.write(f"Processed {file_count} files...\n")

                    try:
                        src_file_path = os.path.join(root, file)
                        dst_file_path = os.path.join(dst_dir, file)

                        # Rename file if it already exists in destination
                        if os.path.exists(dst_file_path):
                            unique_name = unique_file(dst_dir, file)
                            dst_file_path = os.path.join(dst_dir, unique_name)

                        shutil.move(src_file_path, dst_file_path)
                        total_files_moved += 1
                    except Exception as e:
                        log_file.write(f"Failed to move {src_file_path}: {e}\n")

        # Logging summary
        log_file.write(f"Total folders processed: {folder_count}\n")
        log_file.write(f"Total files detected: {file_count}\n")
        log_file.write(f"Total files moved: {total_files_moved}\n")
        log_file.write(f"File types detected: {', '.join(file_types_detected)}\n")

# Example usage
source_directory = 'C:/Users/Horatio/Desktop/source' # Change this to your source directory
destination_directory = 'C:/Users/Horatio/Desktop/target' # Change this to your destination directory
file_extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG', '.mp4', '.MP4', '.avi', '.AVI', '.gif', '.GIF', '.thm', '.THM', '.ppt', '.PPT', '.pptx', '.PPTX', '.bmp', '.BMP', '.eps', '.EPS', '.pdf', '.PDF', '.tif', '.TIF', '.tiff', '.TIFF', '.eps', '.EPS', '.raw', '.RAW', '.3gp', '.3GP', '.mov', '.MOV', '.psd', '.PSD', '.mpg', '.MPG', '.emf','.EMF', '.amr', '.AMR', '.wmf', '.WMF'] # Add or remove file types as needed
log_file = 'C:/Users/Horatio/Desktop/log_file.txt' # Path to your log file

move_files_in_batches(source_directory, destination_directory, file_extensions, log_file)
