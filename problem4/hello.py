for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        prod = i * j
        if str(prod) == str(prod)[::-1]:
            print(prod)
            exit()