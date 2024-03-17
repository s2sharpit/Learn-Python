x = 10


def func():
    global x
    x = 20
    y = 11

    def func2():
        nonlocal y
        y = 30
        print('Nested Function', y)

    func2()
    print('Inner', x)


func()
print('Outer', x)