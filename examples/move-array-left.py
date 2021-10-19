def array_move_left(A: list, N: int):
    """
    Move the elements of an array
    left in a cycle.
    :param A: list
    :param N: number of elements
    :return: none
    """

    tmp = A[0]
    for k in range(N - 1):
        A[k] = A[k + 1]
    A[N - 1] = tmp


def test1_array_move_left():
    A = [1, 2, 3, 4, 5]
    B = [2, 3, 4, 5, 1]
    array_move_left(A, 5)
    if A == B:
        print("test1-ok")
    else:
        print("test1-fail")
        print(A)


test1_array_move_left()
