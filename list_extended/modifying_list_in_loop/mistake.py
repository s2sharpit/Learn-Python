people: list[str] = ['Mario', 'Luigi', 'Peach', 'Toad']

for person in people:
    if person == 'Luigi':
        people.remove('Luigi')
    
    if person == 'Peach':
        print('Hi from Peach')

    print(person, '->', people)