from unittest import TestCase

import binary_serach


class Test(TestCase):
    def test_left_bound(self):
        test_array = [0, 1, 2, 3, 4, 5, 6, 7]
        actual = 5
        expected = binary_serach.binary_search(test_array, 5)
        self.assertEqual(actual, expected)
