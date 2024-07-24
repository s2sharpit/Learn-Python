# Deleting Files

import os

# if os.path.exists("14_file_management/name.txt"):
#     os.remove("14_file_management/name.text")


# for file in os.listdir("sample_folder"):
#     if file.endswith(".txt"):
#         os.remove(f"sample_folder/{file}")
#         print(f"{file} has been deleted")
#     else:
#         print(f"{file} is not a text file")


# folder_name = "sample_folder/"
# for file in os.listdir(folder_name):
#     if os.path.exists(folder_name + file):  # check if the file exists
#         try:
#             os.remove(folder_name + file)
#             print(f"{file} has been deleted")
#         except Exception as e:
#             print(f"Error: {e}")
#     else:
#         print(f"{file} doesn't exist")


os.rmdir("sample_folder")  # Remove the directory