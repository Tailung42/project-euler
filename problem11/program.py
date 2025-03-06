def main():
    with open("grid.txt", "r") as file:
        content = file.read().strip()
    get_array(content)


def get_row(content):
    row = 0
    for char in content:
        if char == " ":
            row += 1
        if char == "\n":
            row += 1
            break
    return row


def get_column(content):
    column = 0

    for char in content:
        if char == "\n":
            column += 1
    return column + 1


def get_array(content):
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
        for num in arr:
            # print(num, end=" ")



if __name__== "__main__":
    main()