def is_simple_number(x: int):
    """
    Check if x is a simple number.
    :parameter x is positive integer.
    :return bool
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def prime_numbers(x: int):
    """
    Prints the prime numbers up to x by
    Eratosten method.
    :param x: input
    :return: A:list with the prime numbers
    """
    A = [True] * x
    A[0] = A[1] = False
    for i in range(2, x, 1):
        if is_simple_number(i):
            for m in range(2 * i, x, i):
                A[m] = False
    n = 0
    for k in range(x):
        print(k, "is prime" if A[k] else "is not prime")
        if A[k]:
            n += 1

    B = [0] * n
    n = 0
    for k in range(x):
        if A[k]:
            B[n] = k
            n += 1
    return B


def test_prime_numbers():
    x = 21
    A = [2, 3, 5, 7, 11, 13, 17, 19]
    B = prime_numbers(x)
    print(B)
    if A == B:
        print("test-ok")
    else:
        print("test-fail")


test_prime_numbers()
