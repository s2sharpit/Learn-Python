def people(age, *args):
    print(args, age)
    print(type(args))
    for i in args:
        print(i)
    
people(21, 'Tushar', 'Rahul', 'Rajesh', 'Ramesh')