import unittest


def fib(n):
    """
    Calculates Fibonacci number.
    Throws TypeError exception if called with not integer.
    Throws ValueError exception if called with a negative or larger than contracted number.
    :param n: integer from 0 to 9999
    :return: integer from 0 to ...
    """
    pass


class TestFibonacci(unittest.TestCase):

    def test_simple(self):
        for param, result in [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55)]:
            self.assertEqual(fib(param), result)

    def test_stress(self):
        pass

    def test_negative(self):
        pass

    def test_wrong_param_type(self):
        pass


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
