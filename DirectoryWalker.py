import os

def collect_file_names(starting_path, output_file="file_list.txt"):
    file_names = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(starting_path):
        for file in files:
            file_names.append(file)

    # Write file names to the output file
    with open(output_file, "w") as f:
        for file_name in file_names:
            f.write(file_name + "\n")
    
    print(f"File names have been saved to '{output_file}'.")

if __name__ == "__main__":
    # Get the path from the user
    folder_path = input("Enter the folder path: ").strip()

    # Validate the path
    if not os.path.exists(folder_path):
        print("The provided path does not exist. Please check and try again.")
    else:
        collect_file_names(folder_path)
