# GOAL
# - Find the sum of first eleven truncatable primes
# truncatable primes are multidigit primes that can be truncated from left to right or right to left, and they still remain primes.


def main():
    num_of_truncatable_primes = 11
    primes_list = get_two_digit_primes(num_of_truncatable_primes)
    print(f"First {num_of_truncatable_primes} truncatable primes: {primes_list}")
    print(f"\nSum: {sum(primes_list)}")


def get_two_digit_primes(num_of_primes):
    first_two_digit_num = 10
    primes_list = list()
    num = first_two_digit_num

    while len(primes_list) < num_of_primes:
        if is_truncatable_prime(num):
            primes_list.append(num)
        num += 1

    return primes_list


def is_truncatable_prime(num):
    if not is_prime(num):
        return False

    # check for truncations from left
    left_truncated_num = truncate_left(num)
    while left_truncated_num > 0:
        if not is_prime(left_truncated_num):
            return False
        if left_truncated_num < 10:
            break
        left_truncated_num = truncate_left(left_truncated_num)

    # check for truncations from right
    right_truncated_num = truncate_right(num)
    while right_truncated_num > 0:
        if not is_prime(right_truncated_num):
            return False
        if right_truncated_num < 10:
            break
        right_truncated_num = truncate_right(right_truncated_num)

    return True


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def truncate_left(num):
    return num % (10 ** (len(str(num)) - 1))


def truncate_right(num):
    return num // 10


if __name__ == "__main__":
    main()
