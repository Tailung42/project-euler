from utils import *

def main():
    with open("grid.txt", "r") as file:
        content = file.read().strip()
    get_array(content)


if __name__== "__main__":
    main()