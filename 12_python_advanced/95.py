# Assert

def start_program(data: dict):
    """This starts the program"""
    assert isinstance(data, dict), "Invalid JSON"
    assert data, "No data found..."

    print("Program loaded successfully!")


if __name__ == "__main__":
    json: dict = {"name": "mario"}

    start_program(json)

    print(__debug__)


# run in command line
     
# python -O 95.py
# runs the program without the assertions (optimized mode), debug mode is off
    
# python -OO 95.py
# runs the program without the assertions and the docstrings (optimized mode), debug mode is off