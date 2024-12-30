lower_limit = 100
upper_limit = 999

def main():
    greatest_palindrome, num1_result, num2_result = 0, 0, 0
    for num1 in range(upper_limit, lower_limit-1, -1):
        for num2 in range(num1, lower_limit-1, -1 ):
            product = num1 * num2
            if product < greatest_palindrome:
                break # products will get smaller
            if is_palindrome(product):
                greatest_palindrome = product
                num1_result,num2_result = num1, num2
                break # no need to continue for smaller num2

        # Once a palindrome is found, products with smaller num1 values will not exceed it
        # if num1 < upper_limit / 2 and greatest_palindrome:
        #     break

    if greatest_palindrome:
        print(f"Greatest palindrome product {num1_result} * {num2_result} = {greatest_palindrome}")
    else:
        print("there is no palindrome within the range")


def is_palindrome(num):
    string = str(num)
    return string == string[::-1]


main()