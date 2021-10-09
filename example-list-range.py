A = [1, 2, 3, 4, 5]


def print_list(A: list, N: int):
    """
    Print the list A with N elements
    to practice with range function.
    Print last element
    """
    for i in range(N):
        print(A[i])

    # print last element
    print(A[N - 1])


print_list(A, 5)
