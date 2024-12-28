# DirectoryWalker

**DirectoryWalker** is a lightweight Python script that recursively scans a given directory and its subdirectories to collect file names. It outputs a list of all discovered file names into a text file for easy reference.

## Features
- Recursively traverses all folders and subfolders starting from a specified path.
- Collects and saves all file names to a `.txt` file.
- Simple and easy to use.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository:
```bash
git clone https://github.com/yourusername/DirectoryWalker.git
cd DirectoryWalker
```
   
2. Run the script:
```bash
python collect_files.py
```

3. Enter the folder path you would like to explore.

## Example Output
If the directory contains the following structure:
```
/example-folder
  ├── subfolder1
  │     ├── file1.txt
  │     ├── file2.docx
  ├── subfolder2
        ├── file3.png
```
The file_list.txt will contain:
```
file1.txt
file2.docx
file3.png
```
