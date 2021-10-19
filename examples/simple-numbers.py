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


def test_is_simple_number():
    A = [2, 3, 5, 7, 11, 17, 19]
    for i in range(7):
        if not is_simple_number(A[i]):
            print("test-fail")
            break
    print("test-ok")


test_is_simple_number()
