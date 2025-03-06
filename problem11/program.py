def main():
    with open("grid.txt", "r") as file:
        content = file.read().strip()
    get_array(content)


def get_row(content):
    """returns the no. of rows in the content grid"""
    row = 0
    for char in content:
        if char == " ":
            row += 1
        if char == "\n":
            row += 1
            break
    return row


def get_column(content):
    """returns the no. of column in the conent grid"""
    column = 0

    for char in content:
        if char == "\n":
            column += 1
    return column + 1


def get_array(content):
        """ reads all space separated numbers from string and returns a list of number"""
        row = get_row(content)
        column = get_column(content)
        arr = [0]*(row * column)
        index = 0
        number = 0

        for char in content:
            if char.isnumeric():
                number = number * 10 + int(char)
            else:
                arr[index] = number
                number = 0
                index += 1
        arr[index] = number  # ensures the final number is added to the array
        return arr

if __name__== "__main__":
    main()