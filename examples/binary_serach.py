"""
Binary search
"""


def binary_search(A, key):
    left = 0
    right = len(A) - 1
    mid = 0
    while left <= right:
        middle = (left + right) // 2
        # if key is greater, ignore left half
        if A[middle] < key:
            left = middle + 1
        # else ignore right half
        elif A[middle] > key:
            right = middle - 1
        else:
            return middle


if __name__ == "__main__":
    print(binary_search([0, 1, 2, 3, 4, 5, 6, 7], 7))
