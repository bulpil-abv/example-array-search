def is_simple_number(x: int):
    """
    A prime number (or a prime) is a natural number
    greater than 1 that is not a product of two smaller natural numbers.
    Check if x is a prime number.
    :parameter x is positive integer.
    :return bool
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def test_is_prime_number():
    A = [2, 3, 5, 7, 11, 17, 19]
    for i in range(7):
        if not is_simple_number(A[i]):
            print("test-fail")
            break
    print("test-ok")


if __name__ == "__main__":
    test_is_prime_number()
