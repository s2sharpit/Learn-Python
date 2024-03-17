# Classes Varaibles & Instance Varaibles
# Class variables are shared among all instances of a class. They are defined within a class but outside any method or block. They are not tied to any particular instance of a class. They are shared among all instances of a class. They are defined within a class but outside any method or block. They are not tied to any particular instance of a class.

# Class variable should be reserved for something you want for all animals to always share and have in common.


class Animal:
    tricks: list[str] = []  # Class Variable

    def __init__(self, name: str):
        self.name = name  # Instance Variable

    def teach_trick(self, trick_name: str):
        self.tricks.append(trick_name)


if __name__ == "__main__":
    dog: Animal = Animal("Dog")
    cat: Animal = Animal("Cat")

    dog.teach_trick("Make Dinner!")
    dog.teach_trick("Go work at a job!")
    cat.teach_trick("I am a cat!")

    print("Dog tricks:", dog.tricks)
    print("Cat tricks:", cat.tricks)
