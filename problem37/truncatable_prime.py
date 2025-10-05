# GOAL
# - Find the sum of first three truncatable primes
# truncatable primes are multidigit primes that  can be truncated from left to right or right to left , and they still remain primes.
import math


def main():
    _num_of_truncatable_primes_ = 11
    get_two_digit_primes(_num_of_truncatable_primes_)


def get_two_digit_primes(num_of_primes):
    _first_two_digit_num_ = 10
    primes_list = list()
    num = _first_two_digit_num_

    while len(primes_list) < num_of_primes:
        if is_truncatable_prime(num):
            primes_list.append(num)
        num += 1
        print(num)


def is_truncatable_prime(num):
    if not is_prime(num):
        return False

    left_truncated_num = truncate_left(num)
    right_truncated_num = truncate_right(num)
    print(f" {num}: {left_truncated_num}, {right_truncated_num}")
    is_prime_from_left = True
    is_prime_from_right = True

    while left_truncated_num > 0:
        if not is_prime(left_truncated_num):
            is_prime_from_left = False
            break
        if left_truncated_num < 10:
            if not is_prime(left_truncated_num):
                is_prime_from_left = False
            break
        left_truncated_num = truncate_left(left_truncated_num)

    while right_truncated_num > 0:
        if not is_prime(right_truncated_num):
            is_prime_from_right = False
            break
        if right_truncated_num < 10:
            if not is_prime(right_truncated_num):
                is_prime_from_right = False
                break
        right_truncated_num = truncate_right(right_truncated_num)

    return is_prime_from_left and is_prime_from_right


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def truncate_left(num):
    return num % 10 ** (len(str(num)) - 1)


def truncate_right(num):
    return num // 10


if __name__ == "__main__":
    main()


# take a number
# get it's right truncated num
# get it's left truncated num
# check if rtn is prime and rtn of (rtn is prime)
