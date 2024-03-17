# eval()   evaluate

problem: str = """
10 * 'hello'
"""
print(eval(problem))

user_input: str = input("Insert your maths: ")
result: float = eval(user_input)
print(result)
