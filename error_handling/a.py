user_input = input('Enter a number: ')

# try:
#     number = float(user_input)
#     print(number)
# except Exception as e:
#     print(e)


try:
    number = float(user_input)
    result = number / 0
    print(number)
except ValueError:
    print('Please enter a valid number!')
except ZeroDivisionError:
    print('Please enter a non-zero number!')
except Exception as e:
    print('Something went wrong!', e)