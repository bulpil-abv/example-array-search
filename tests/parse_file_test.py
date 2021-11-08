import unittest

from parse_file import *


class TestParseFile(unittest.TestCase):
    def test_parse_file_line(self):
        path = "D:\\blender_scripts\\blender_repo\output from digitizer\sec_01 70 data pts.txt"
        expected = (32.5581395348837, 297.692307692308, 476.25)  # dataset[2]
        actual = parse_file(path)[2]
        self.assertEqual(actual, expected)

    def test_parse_file_last_line(self):
        path = "D:\\blender_scripts\\blender_repo\output from digitizer\sec_01 70 data pts.txt"
        expected = (0.00000000000000, -297.692307692308, 476.25)
        actual = parse_file(path)[-1]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
