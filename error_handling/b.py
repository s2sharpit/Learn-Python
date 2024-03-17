def do_math():
    user_input = input('Enter a number: ')
    try:
        number = float(user_input)
        print(number)
    except ValueError:
        print('Please enter a valid number!')
        do_math()
    except Exception as e:
        print('Something went wrong!', e)
    else:
        print('Successfully executed code!')


do_math()