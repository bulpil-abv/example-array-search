import unittest
from recipe_TDD import *

class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_integer(self):
        self.assertEqual(nitro_salt(1000),10)


if __name__ == '__main__':
    unittest.main()
