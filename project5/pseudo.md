problem: find the smallest multiple of N natural numbers:
eg. the LCM of numbers upto 20 is 2520;

pseudocode 1: 

    1 - find the lcm of last  two numbers and then the lcm of (lcm and third last number) and the lcm of that (lcm and fourth last number) and so on up to 1  -- seems recurssive

    2 how do You find the lcm of two numbers?

        lcm(a, b) = a*b / hcf(a, b)

    3 - how do you find the hcf to two numbers a, b?

        hcf(a, b):
            # input: a, b such that a <= b
            # output: hcf of a and b

            for divisor from a down to 1:
                if a % divisor == 0 and b% divisor == 0:
                    return divisor
            

            alternatively,
            
            for divisor from 1 up to a:
            if  a % divisor == 0 then:
                quotient = a / divisor
                if b % divisor == quotient:
                return quotient



new algorith to find hcf between any two numbers:
    let a, b be two numbers such that a <= b
    input: a,b
    output: hcf(a,b)

    if b%a == 0 then
         return a as the hcf
    else:
    factor = integer_factor(b/a):  # integer factor of a decimal number is 
    hcf = a / factor
    

    integer_factor(quotient):
        if quotient is an integer
            return 1

        decimal_part = quotient % 1
        int_factor = 1 / decimal_part
        if quotient * int_factor is approximately an integer:
            return int_factor
        else:
            return int_factor * integer_factor(quotient* int_factor)

        
