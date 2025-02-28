import sys

def main():
    # if no. of arguments is not 2 then return error message
    if not len(sys.argv) == 2:
        print("Usage: program.py limit(int)")
        return
    
    limit = int(sys.argv[1])
    even_sum = sum_even_fibonacci(limit)

    print(f"sum of even fibonacci numbers upto {limit} is {even_sum}")


def sum_even_fibonacci(limit):
    current = 0
    nxt = 1
    temp = int()
    even_sum= 0
    while current <= limit:
        if current % 2 == 0:
            even_sum += current
        
        # update the terms 
        temp = current + nxt
        current = nxt
        nxt = temp
    return even_sum


if __name__ == "__main__":
    main()