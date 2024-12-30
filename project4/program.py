lower_limit = 100
upper_limit = 999

def main():
    greatest_palindrome = 0
    for num1 in range(upper_limit, lower_limit-1, -1):
        for num2 in range(num1, lower_limit-1, -1 ):
            product = num1 * num2
            if is_palindrome(product) and product > greatest_palindrome:
                greatest_palindrome = product
                break  # num1 * (num2 - any number ) will always yield smaller result
            
        # if palindrome is found and we've checked all upper half no need to check lower half
        if num1 < upper_limit / 2 and greatest_palindrome:
            break
    if greatest_palindrome:
        print(f"Greatest palindrome product: {greatest_palindrome}")
    else:
        print("there is no palindrome within the range")


def is_palindrome(num):
    string = str(num)
    return string == string[::-1]


main()