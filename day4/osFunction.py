import os

print("Current Working Directory:", os.getcwd())
print("List of files and directories in the current directory:", os.listdir('.'))

# Create a new directory
new_dir = 'test_directory'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Directory '{new_dir}' created.")
else:     
    print(f"Directory '{new_dir}' already exists.")


#check if a file exists
file_path = 'test_file.txt'

print(f"File '{file_path}' exists.")


#remove a directory
