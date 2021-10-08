def array_search(Ar: list, N: int, x: int):
    """ Search Ar from 0 to N-1
    to find the index of first x if any.
    If x is not in Ar, return -1"""
    for i in range(N):
        if Ar[i] == x:
            return i
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1-ok")
    else:
        print("#test1-fail")

    A2 = [1, 2, 3, 4, 5]
    m = array_search(A2, 5, 3)
    if m == 2:
        print("#test2-ok")
    else:
        print("#test2-fail")

    A3 = [1, 1, 1, 1, 1]
    m = array_search(A3, 5, 1)
    if m == 0:
        print("#test3-ok")
    else:
        print("#test1-fail")


test_array_search()
