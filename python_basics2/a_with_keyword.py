# file = open('a_sample.text')
# text = file.read()
# file.close()

# print(text)

with open('python_basics2/a_sample.text') as file:
    text = file.read()
    print(text)