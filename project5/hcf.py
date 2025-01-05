import sys
step = 0


# this is my algorithm to find hcf 

def my_hcf(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    factor = find_factor(num1/num2)
    print(int(num2/factor))
    print(f'steps {step}')

def find_factor(num):
    global step  
    step += 1
    if num.is_integer():
        return 1

    factor = 1/ (num % 1)

    if approximately_integer(factor):
        return round(factor)
    return round(factor * find_factor(factor))


def approximately_integer(num):
    return abs(num - int(num)) < 0.00001




# this is euclidian algorithm
# probably the most efficient one

def euclidian_hcf(num1, num2):
    if num2 > num1:
        num2, num1 = num1, num2
    print(find_hcf(num1, num2))
    print(f"step {step}")

# the actual algorithm 
def find_hcf(num1, num2):
    """find the hcf of num1 and num2"""
    # improved algorithm Euclidian algorithm
    #time complexity = O(log(smaller number))
    global step 
    step += 1
    if num2 == 0:
        return num1
    return find_hcf(num2, num1%num2)

        
# if __name__ == "__main__":
    # my_hcf(int(sys.argv[1]), int(sys.argv[2]))
    # euclidian_hcf(int(sys.argv[1]), int(sys.argv[2]))