import unittest
import app.io.input as inp


class TestReadFromFileUsingPandas(unittest.TestCase):
    def test_dataframe_not_empty(self):
        data_frame = inp.read_from_file_using_pandas("../data/pandas_data.csv")
        self.assertFalse(data_frame.empty, "Data frame isn't empty ")

    def test_dataframe_columns(self):
        expected_columns = ["id", "first_name", "last_name", "email", "gender", "ip_address"]
        data_frame = inp.read_from_file_using_pandas("../data/pandas_data.csv")
        self.assertListEqual(list(data_frame.columns), expected_columns, "Columns should match")

    def test_dataframe_shape(self):
        expected_shape = (10, 6)
        data_frame = inp.read_from_file_using_pandas("../data/pandas_data.csv")
        self.assertEqual(data_frame.shape, expected_shape, "Shape should match")


if __name__ == '__main__':
    unittest.main()
