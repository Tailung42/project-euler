import sys
import math

def main():
    if len(sys.argv) != 2:
        print("Usage: program.py Integewr")
        return
    number = int(sys.argv[1])

    factor = get_prime_factor(number)
    print(f"Largest prime Factor of {number} is {factor}")


def get_prime_factor(num):
    largest = int() # create an int 
    
    for i in range(int(math.sqrt(num)) + 1):
        if is_prime(i):
            if num % i == 0:
                largest = i
    return largest if largest else None



def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    else:
        return True
    

if __name__ =="__main__":
    main()