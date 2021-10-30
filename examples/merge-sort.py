def merge_sort(A: list):
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
    return A


def merge(A: list, B: list):
    """
    Merges sorted lists.
    Returns a sorted list.
    :param A:
    :param B:
    :return:
    """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n]=B[k]
            k+=1
            n+=1
    while i<len(A):
        C[n]=A[i]
        i+=1
        n+=1
    while k<len(B):
        C[n]=B[k]
        k+=1
        n+=1
    return C

def test_merge_sort():
    A = [90, 3, 3, 5, 7, 13,0]
    B = [0,3, 3, 5, 7, 13, 90]
    C = merge_sort(A)
    print("A test-input",A)
    print("B test-sorted",B)
    print("C mergesort-sorted",C)
    print("Test Ok" if B == C else "Test Fail")


if __name__ == "__main__":
    test_merge_sort()
