import os

def rename_files_with_numbers(folder_path, start_number=1, increment=1):
    if not os.path.isdir(folder_path):
        print("The provided path is not a valid directory.")
        return

    file_list = os.listdir(folder_path)
    file_list.sort()  # Ensure consistent sorting order

    for index, filename in enumerate(file_list, start=start_number):
        name, extension = os.path.splitext(filename)
        new_name = f"{index:03d}{extension}"  # Using zero-padded numbers (e.g., 001, 002, ...)
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

    print(f"Renamed {len(file_list)} files.")

# Provide the folder path where your files are located
folder_path = "C:\\Desktop\\Trading images"
rename_files_with_numbers(folder_path, start_number=1, increment=1)
