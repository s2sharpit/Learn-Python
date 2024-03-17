# exec()    execute

# user_input: str = input("Your code: ")
# exec(user_input)

user_defined_code: str = """
x = 10
print(x)

for i in range(10):
    print(i, end=" ")
"""
exec(user_defined_code)
