


def find_hcf(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for i in range( num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
        
find_hcf(9, 3)
