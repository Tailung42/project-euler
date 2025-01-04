def main():
    # time complexity: O(n)
    natural_nubers = 4   
    lcm = natural_nubers
    for i in range(natural_nubers-1 , 0, -1):
        if lcm % i != 0:
            lcm = find_lcm(lcm, i)

    print(int(lcm))



def find_lcm(num1, num2):
    # time complexity O(1)
    return (num1 * num2) / find_hcf(num1, num2)


def find_hcf(num1, num2):
    # the algorithm needs to be improved 
    # timecomplexity is O(n):
    if num1 > num2:
        num1, num2 = num2, num1
    for i in range( num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
        
find_hcf(9, 3)

if __name__ == "__main__":
    main()