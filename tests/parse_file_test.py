import unittest

from parse_file import *


class TestParseFile(unittest.TestCase):
    def test_parse_file_line(self):
        path = ["D:\\blender_scripts\\blender_repo\output from digitizer\sec_01 70 data pts.txt"]
        expected = [32.5581395348837, 297.692307692308, 476.25]  # dataset[2]
        actual = parse_file(path)[2]
        self.assertEqual(actual, expected)

    def test_parse_file_last_line(self):
        path = ["D:\\blender_scripts\\blender_repo\output from digitizer\sec_01 70 data pts.txt"]
        expected = [0.00000000000000, -297.692307692308, 476.25]
        actual = parse_file(path)[-1]
        self.assertEqual(actual, expected)

    def test_parse_multiple_files(self):
        """
        files = ["D:\\blender_scripts\\blender_repo\output from digitizer\sec_01 70 data pts.txt",
                 "D:\\blender_scripts\\blender_repo\output from digitizer\sec_02 70 data pts.txt",
                 "D:\\blender_scripts\\blender_repo\output from digitizer\sec_03 70 data pts.txt",
                 "D:\\blender_scripts\\blender_repo\output from digitizer\sec_04 70 data pts.txt",
                 "D:\\blender_scripts\\blender_repo\output from digitizer\sec_05 70 data pts.txt",
                 "D:\\blender_scripts\\blender_repo\output from digitizer\sec_06 70 data pts.txt"]
        """
        files = ["D:\\blender_scripts\\blender_repo\output from digitizer\\test_sec_01 15 data pts.txt",
                 "D:\\blender_scripts\\blender_repo\output from digitizer\\test_sec_02 15 data pts.txt"]
        expected = [[0.0, 5.0, 0.0],
                    [0.5, 5.0, 0.0],
                    [1.0, 4.5, 0.0],
                    [1.5, 4.0, 0.0],
                    [2.0, 3.0, 0.0],
                    [2.0, 2.0, 0.0],
                    [2.0, 1.0, 0.0],
                    [2.0, 0.0, 0.0],
                    [2.0, -1.0, 0.0],
                    [2.0, -2.0, 0.0],
                    [2.0, -3.0, 0.0],
                    [1.5, -4.0, 0.0],
                    [1.0, -4.5, 0.0],
                    [0.5, -5.0, 0.0],
                    [0.0, -5.0, 0.0],
                    [0.0, 5.0, 1.0],
                    [0.5, 5.0, 1.0],
                    [1.0, 4.5, 1.0],
                    [1.5, 4.0, 1.0],
                    [2.0, 3.0, 1.0],
                    [2.0, 2.0, 1.0],
                    [2.0, 1.0, 1.0],
                    [2.0, 0.0, 1.0],
                    [2.0, -1.0, 1.0],
                    [2.0, -2.0, 1.0],
                    [2.0, -3.0, 1.0],
                    [1.5, -4.0, 1.0],
                    [1.0, -4.5, 1.0],
                    [0.5, -5.0, 1.0],
                    [0.0, -5.0, 1.0]]
        actual = parse_file(files)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
