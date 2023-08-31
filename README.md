# File Renaming Script

This script is designed to help you rename files in a specified folder with numbered filenames. It's particularly useful when you want to add a numerical sequence to a batch of files, such as images, to organize them or prepare them for further processing.

## Usage

1. Make sure you have Python installed on your system.
2. Replace `"C:\\Desktop\\Trading images"` in the `folder_path` variable with the actual path of the folder containing the files you want to rename.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command: `python script_name.py` (replace `script_name.py` with the actual name of the script file).

## Script Explanation

The script accomplishes the following:

1. It starts by checking whether the provided `folder_path` is a valid directory.
2. It retrieves the list of files in the directory and sorts them to ensure consistent renaming order.
3. For each file in the list, it extracts the file name and extension.
4. It constructs a new file name using a numbering scheme (e.g., 001, 002, ...) and the original extension.
5. The script renames the file by moving it from the old path to the new path using `os.rename`.
6. After all files have been renamed, the script provides feedback about the renaming process, including the old and new file names.

## Parameters

- `folder_path`: Replace this variable with the path to the folder containing the files you want to rename.
- `start_number`: The initial number to start the renaming sequence from (default: `1`).
- `increment`: The amount by which the numbering should increase with each file (default: `1`).

Please ensure that you have a backup of your files before running the script, as renaming files can be irreversible.

**Note:** This script is provided as-is, and the author shall not be responsible for any unintended consequences that may arise from its usage. Make sure to test the script on a small set of files before using it on a larger scale.
