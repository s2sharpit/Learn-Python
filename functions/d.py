def do_something(**kwargs):
    print(kwargs)
    print(kwargs['name'])

do_something(name='Tushar', age=21, city='Delhi')