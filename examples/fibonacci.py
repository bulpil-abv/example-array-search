def fib(n):
    """
    Calculates Fibonacci number with list.
    :param n: not negative whole number
    :return: number
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work only with class <int> type.")
    if n < 0:
        raise ValueError("Fibonacci can't work with negative numbers.")
    if n >= 10000:
        raise ValueError("Fibonacci can't work with numbers larger than 9999.")
    if n < 2:
        return n

    F = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]



def fib_recursive(n):
    """
    Calculates Fibonacci number by recursion.
    :param n: not negative whole number
    :return: number
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work only with class <int> type.")
    if n < 0:
        raise ValueError("Fibonacci can't work with negative numbers.")
    if n >= 10000:
        raise ValueError("Fibonacci can't work with numbers larger than 9999.")
    if n < 2:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
