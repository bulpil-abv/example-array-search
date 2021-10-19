def array_move_right(A: list, N: int):
    """
    Shift the elements of the array right
    in a cycle.
    :param A: input list
    :param N: number of elements
    :return: none
    """

    tmp = A[N - 1]
    for i in range(N):
        A[N - 1 - i] = A[N - 2 - i]
    A[0] = tmp


def test_array_move_right():
    A = [1, 2, 3, 4, 5]
    B = [5, 1, 2, 3, 4]

    array_move_right(A, 5)

    if A == B:
        print("test1-ok")
    else:
        print("test1-fail")
        print(A)


test_array_move_right()
