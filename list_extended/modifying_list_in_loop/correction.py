people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
people2: list[str] = []

for person in people:
    print(person, "->", people2)

    if person != "Luigi":
        people2.append(person)

    if person == "Peach":
        print("Hi from Peach")

print(people2)