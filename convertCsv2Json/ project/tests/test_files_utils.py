import unittest
import json
from files_utils import read_csv, write_json


class TestCSVUtils(unittest.TestCase):

    def test_read_csv_valid_file(self):
        csv_file = 'test_files/csv_file.csv'
        delimiter = ','
        header, csv_data = read_csv(csv_file, delimiter)
        # Strip every string in the header
        stripped_header = [column.strip() for column in header]
        # Assert expected values in header
        self.assertEqual(stripped_header, ['firstName', 'lastName', 'age', 'gender', 'isMarried'])
        # Assert 3 rows in the test CSV file
        self.assertEqual(len(csv_data), 3)

    def test_read_csv_invalid_file(self):
        csv_file = 'test_files/nonexistent.csv'
        delimiter = ','

        # Use assertRaises to check if the function raises the expected exception
        with self.assertRaises(FileNotFoundError):
            read_csv(csv_file, delimiter)


class TestJSONUtilsTests(unittest.TestCase):
    def test_write_json_valid_data(self):
        json_data = [
            {"firstName": "jana", "lastName": "nemcova", "age": "32", "gender": "F", "isMarried": False},
            {"firstName": "lucka", "lastName": "motykova", "age": "30", "gender": "F", "isMarried": False},
            {"firstName": "misa", "lastName": "vondrackova", "age": "31", "gender": "F", "isMarried": True}
        ]
        json_file = 'test_files/json_file.json'
        encoding = 'utf-8'

        # Write test data to the JSON file
        write_json(json_data, json_file, encoding)

        # Read the JSON file to verify the content
        with open(json_file, 'r', encoding=encoding) as file:
            loaded_data = json.load(file)

        # Assert expected values
        self.assertEqual(loaded_data, json_data)

    def test_write_json_invalid_data(self):
        json_data = set()  # JSON serialization does not support sets
        json_file = 'test_files/invalid_output.json'
        encoding = 'utf-8'

        # Use assertRaises to check if the function raises the expected exception
        with self.assertRaises(TypeError):
            write_json(json_data, json_file, encoding)


if __name__ == '__main__':
    unittest.main()
