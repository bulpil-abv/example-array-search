import unittest


def check_sorted(A: list, ascending=True) -> bool:
    """
    Checks if Array A is sorted
    :param A: list
    :return: true or false
    """
    flag = True
    for i in range(0, len(A)-1):
        if A[i] > A[i + 1]:
            flag = False
            break
    return flag


class TestCheckSorted(unittest.TestCase):
    def test_check_sorted(self):
        expected = True
        actual = check_sorted([1, 2, 3, 4, 5, 6])
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
