# Match case

status: int = 403

if status == 400:
    print("Bad request...")
elif status == 403:
    print("Forbidden...")
elif status == 404:
    print("Not found...")
else:
    print("Something went wrong...")

match status:
    case 400:
        print("Bad request...")
    case 403:
        print("Forbidden...")
    case 404:
        print("Not found...")
    case _:
        print("Something went wrong...")