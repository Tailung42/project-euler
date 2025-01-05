import sys

def hcf(num1 = 1000, num2 = 3):
    if num1 > num2:
        num1, num2 = num2, num1  # make num1 the smaller value
    if num2 % num1 == 0: # check if num1 itself is the HCF
        print(num1)
        return num1
    factor = integer_factor(num2/num1)
    print(round( num2 / factor))


def integer_factor(quotient):
    print(f"quotient: { quotient}")

    if quotient.is_integer():
        return 1
    decimal_part = quotient % 1
    int_factor = 1 / decimal_part
    print(f"multiplying factor {int_factor}")
    product = int_factor * quotient
    print( "supposed integer " + str(product) + "\n")
    if approximately_integer(product , 0.00001):
        return product
    else:   
        return integer_factor(product)


def approximately_integer(num, tolerence):
    """ returns if a float is approximately integer or not \n tolerence -> How much error is toleratable"""
    return abs(num - round(num)) < tolerence



hcf(int(sys.argv[1]), int(sys.argv[2]))


