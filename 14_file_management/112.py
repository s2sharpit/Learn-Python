# Writing & Creating files

# with open("14_file_management/sample.text", "a+") as text: # a+ is for appending and reading
# '''Create the file if not exists and append the text to the file'''
#     text.write("\nNew text")
#     text.seek(0) # Move the cursor to the beginning of the file
#     print(text.read())

# with open("14_file_management/name.text", "w+") as text:
#     '''Create the file if not exists and write the text to the file replacing the existing text'''
#     text.write("12345")
#     text.seek(0)
#     print(text.read())

with open("14_file_management/hello.text", "x+") as text:
    """
    Get File Exist Error if the file already exists and try to create the file again
    x is used to create the file if not exists and raise an error if the file already exists
    x+ is used to create the file if not exists and raise an error if the file already exists and read the file
    """
    text.write("Hello World")
    text.seek(0)
    print(text.read())
