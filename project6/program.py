# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum of first one hundred natural 

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 programlpy <number>")
        return 

    try:
        num = int(sys.argv[1])
        if num < 1:
            raise ValueError("Number must be a positive integer")
    except ValueError as e:
        print(f"invalid Input: {e}")
        
        
    diff = abs(sum_of_square_natural(num) - square_sum_of_natural_numbers(num))
    
    print(f"the difference btn sum of squares and square of sum for first {num} natural numbers is: {diff}")


def square_sum_of_natural_numbers(n):
    return (n * (n + 1) // 2)**2

def sum_of_square_natural(n):
    return n * (n + 1) * (2 * n + 1) // 6


if __name__ == "__main__":
    main()