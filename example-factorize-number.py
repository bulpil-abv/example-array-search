def factorize_number(x: int):
    """
    Finds divisors of a number
    :param x: positive whole number
    :return: A list of divisors
    """
    k = 0
    B = [0] * (x // 2)
    for i in range(1, x + 1, 1):
        if x % i == 0:
            B[k] = i
            k += 1
    return B


def test1_factorize_number():
    x = 21
    A = [1, 3, 7, 21, 0, 0, 0, 0, 0, 0]
    B = factorize_number(x)
    if A == B:
        print("test1-ok")
    else:
        print("test1-fail")
    print(B)


def test2_factorize_number():
    x = 10
    A = [1, 2, 5, 10, 0]
    B = factorize_number(x)
    if A == B:
        print("test2-ok")
    else:
        print("test2-fail")
    print(B)


test1_factorize_number()
test2_factorize_number()