import os

def rename_images(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found.")
        return

    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Add more extensions if needed
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))
                   and any(f.lower().endswith(ext) for ext in image_extensions)]

    if len(image_files) == 0:
        print("No image files found in the folder.")
        return

    image_files.sort()  # Sort files to maintain order

    for index, image_file in enumerate(image_files):
        extension = os.path.splitext(image_file)[1]
        new_name = f"Josh_{index+1:03d}{extension}"
        os.rename(os.path.join(folder_path, image_file), os.path.join(folder_path, new_name))
        print(f"Renamed {image_file} to {new_name}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\joshu\\Python"
    rename_images(folder_path)
