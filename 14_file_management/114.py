import json

with open("./14_file_management/sample.json") as file:
    content: dict = json.load(file)
    print(content)
