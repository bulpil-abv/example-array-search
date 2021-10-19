def invert_array(A: list, N: int):
    """
    Invert the array A
    in range from 0 to N-1
    """
    B = [0] * N

    for i in range(N):
        B[i] = A[N-1- i]

    for i in range(N):
        A[i] = B[i]


def test_invert_array():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]
    invert_array(A, 10)
    print(A)
    if A == [1000, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        print("test1-ok")
    else:
        print("test-fail")


test_invert_array()
