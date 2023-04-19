import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# List all files in the current directory
files = os.listdir(cwd)
print(f"Files in the current directory: {files}")

# Create a new directory
new_dir = "my_new_dir"
os.mkdir(new_dir)
print(f"New directory '{new_dir}' created.")

# Rename a file
# old_file = "my_file.txt"
# new_file = "renamed_file.txt"
# os.rename(old_file, new_file)
# print(f"File '{old_file}' renamed to '{new_file}'.")
