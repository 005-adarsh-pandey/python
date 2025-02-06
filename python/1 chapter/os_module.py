import os

# Specify the directory path
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)