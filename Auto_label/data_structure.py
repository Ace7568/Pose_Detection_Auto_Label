import os
import shutil

def copy_images(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate over each subdirectory (0, 1, 2, ...)
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)
        # Check if it's a directory
        if os.path.isdir(subdir_path):
            # Iterate over each image file in the subdirectory
            for image_name in os.listdir(subdir_path):
                # Construct paths for source and destination
                source_path = os.path.join(subdir_path, image_name)
                destination_path = os.path.join(destination_dir, image_name)
                try:
                    # Copy the image to the destination directory
                    shutil.copyfile(source_path, destination_path)
                    print(f"Image '{image_name}' copied successfully.")
                except Exception as e:
                    print(f"Error occurred while copying '{image_name}': {e}")

# Example usage:
source_directory = "./captured_images"  # Directory containing subdirectories 0, 1, 2, ...
destination_directory = "./data/images/train"  # Destination directory for all images

copy_images(source_directory, destination_directory)
