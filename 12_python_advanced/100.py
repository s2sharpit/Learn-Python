# Context Managers

class File:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Opening {self.name}...")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Closing {self.name}")


if __name__ == "__main__":
    with File("file.txt") as file:
        print(file.name)

    print("Done!")
