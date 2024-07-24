# Reading files

with open("14_file_management/sample.text", "r") as text:
    # t: str = text.read()
    # t: str = text.read(10)  # Read the first 10 characters of the file
    # print(t)
    # t1: str = text.readline()
    # t2: str = text.readline()
    # t3: str = text.readline()
    # print(t1)
    # print(t2)
    # print(t3)
    t: list[str] = text.readlines()
    print(t)
    print(text)