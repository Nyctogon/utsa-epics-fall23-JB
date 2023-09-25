import os
import shutil

def create_and_sort_folders(image_sets_root, images_per_folder):
    if not os.path.exists(image_sets_root):
        os.makedirs(image_sets_root)

    for folder_index in range(0, 5):
        folder_name = f"Folder_{folder_index+1}"
        folder_path = os.path.join(image_sets_root, folder_name)
        os.makedirs(folder_path)

        for image_number in range(folder_index * images_per_folder + 1, (folder_index + 1) * images_per_folder + 1):
            image_name = f"Josh_{image_number:02d}.jpg"
            source_path = os.path.join(image_sets_root, image_name)
            destination_path = os.path.join(folder_path, image_name)
            
            if os.path.exists(source_path):
                shutil.move(source_path, destination_path)
                print(f"Moved {image_name} to {folder_name}")

if __name__ == "__main__":
    image_sets_root = "C:\\Users\\joshu\\Python"
    images_per_folder = 10

    create_and_sort_folders(image_sets_root, images_per_folder)
