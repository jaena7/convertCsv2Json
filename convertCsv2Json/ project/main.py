import logging
import os

from config_utils import read_config, get_encoding, get_delimiter
from files_utils import read_csv, process_data, write_json
from logging_utils import setup_logging

if __name__ == "__main__":
    try:
        setup_logging()
        config = read_config()

        def_csv_file_path = config.get('path', 'csv_file')
        csv_file_path = input(
            f"Enter the input path to the CSV file (default is '{def_csv_file_path}'): ") or def_csv_file_path
        csv_file_path = os.path.abspath(os.path.normpath(csv_file_path))

        def_json_file_path = config.get('path', 'json_file')
        json_file_path = input(
            f"Enter the output path to the JSON file (default is '{def_json_file_path}'): ") or def_json_file_path
        json_file_path = os.path.normpath(json_file_path)

        def_delimiter = get_delimiter(config)
        delimiter = input(
            f"Enter the CSV delimiter (default is '{def_delimiter}'): ") or def_delimiter

        def_encoding = get_encoding(config)
        encoding = input(
            f"Enter the JSON encoding (default is '{def_encoding}'): ") or def_encoding

        header, csv_data = read_csv(csv_file_path, delimiter)
        json_data = process_data(header, csv_data)
        write_json(json_data, json_file_path, encoding)

        logging.info("Conversion completed successfully.")
    except Exception as e:
        logging.error(f'An error occurred: {e}')
