import unittest
import app.io.input as inp


class TestReadFromFileUsingPy(unittest.TestCase):

    def test_read_existing_file(self):
        filename = "../data/input_file.txt"
        result = inp.read_from_file_using_py(filename)
        self.assertTrue(len(result) > 0)

    def test_read_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            inp.read_from_file_using_py("non_existing_file.txt")

    def test_count_lines(self):
        filename = "invalid_format_file.xlsx"
        filename = "../data/input_file.txt"
        expected_lines = 4
        result = inp.read_from_file_using_py(filename)
        actual_lines = len(result.split('\n'))
        self.assertEqual(actual_lines, expected_lines)


if __name__ == '__main__':
    unittest.main()
