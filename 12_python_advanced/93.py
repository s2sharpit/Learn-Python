# generators


def generate_list(n: int):
    for i in range(n):
        yield i


if __name__ == "__main__":
    # generator = generate_list(10 ** 100)

    # # print(next(generator))
    # # print(next(generator))
    # # print(next(generator))

    # list_a: list[int] = []
    # for num in generator:
    #     if num == 1000:
    #         break
    #     list_a.append(num)

    # print(len(list_a))
    # # print(list_a)

    generator = generate_list(100)
    list_a: list[int] = []
    for num in generator:
        list_a.append(num)

        if num == 10:
            break
    
    print(list_a)


    list_b: list[int] = []
    for num in generator:
        list_b.append(num)

        if num == 20:
            break
    
    print(list_b)
    # print(next(generator))