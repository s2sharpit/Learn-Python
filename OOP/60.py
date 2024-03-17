# Getters & Setters
# Getter and Setter methods are used to access and modify private attributes of a class. 
# They are also known as accessor and mutator methods. 
# The getter method is used to get the value of a private attribute, and the setter method is used to set the value of a private attribute.
# In python, we can use the property decorator to define getter and setter methods for an attribute.

class Fruit:
    def __init__(self, name: str):
        self._name = name       # underscore means 'name' is treated as a protected 

    @property                   # property decorator allows us to define getter and setter methods for the attribute.
    def name(self):
        print(f'{self._name} is being accessed!')
        return self._name
    
    @name.setter
    def name(self, value: str):
        print(f'{self._name} is now {value}!')
        self._name = value

if __name__ == '__main__':
    apple: Fruit = Fruit('Apple')
    apple.name = 'Banana'
    print(apple.name)