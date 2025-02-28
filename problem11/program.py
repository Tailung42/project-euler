def main():
    with open("grid.txt", "r") as file:
        content = file.read().strip()





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


def give_array(content):
        row = get_row(content)
        column = get_column(content)

        grid = [[0]* column]*row



if __name__== "__main__":
    main()