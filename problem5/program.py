def main():
    # time complexity: O(n)
    natural_nubers = 4   
    lcm = natural_nubers
    for num in range(natural_nubers-1 , 0, -1):
        if lcm % num != 0:
            lcm = find_lcm(lcm, num)

    print(int(lcm))



def find_lcm(num1, num2):
    # time complexity O(1)
    return (num1 * num2) / find_hcf(num1, num2)


def find_hcf(num1, num2):
    """find the hcf of num1 and num2"""
    # improved algorithm Euclidian algorithm
    #time complexity = O(log(smaller number))
    if num2 > num1:
        num2, num1 = num1, num2
    if num2 == 0:
        return num1
    return find_hcf(num2, num1%num2)

        

if __name__ == "__main__":
    main()