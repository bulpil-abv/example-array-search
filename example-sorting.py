# quadratic sorts N-size array -> O(N**2)


def example_insert_sort(A: list):
    """
    N-1 passes
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def example_choice_sort(A: list):
    """
    N-1 passes
    """
    N = len(A)


def example_bubble_sort(A: list):
    """
    N*(N-1)/2 passes
    """


def test_sort(sort_algorithm):
    print("Test: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "fail")  # terniary operator

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("OK" if A == A_sorted else "fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("OK" if A == A_sorted else "fail")


if __name__ == "__main__":
    test_sort(example_insert_sort)
    test_sort(example_bubble_sort)
    test_sort(example_choice_sort)
