def hoar_sort(A):
    """
    Quick sort by Tony Hoare algorithm.
    :param A:
    :return:
    """
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
        hoar_sort(L)
        hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


def test_hoar_sort():
    A = [5, 7, 3, -1, 0, 33, 33, 5]
    B = [-1, 0, 3, 5, 5, 7, 33, 33]
    C = hoar_sort(A)
    print("Test OK" if B == C else "Test fail")


if __name__ == "__main__":
    test_hoar_sort()
