def merge_sort(A):
    """
    Recursively breaking down problem A into
    sub problems until solved directly.
    The solutions are then combined.
    :param A:
    :return:
    """

    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


def merge(A, B):
    pass
