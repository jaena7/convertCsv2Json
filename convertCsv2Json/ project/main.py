import logging

from config_utils import read_config, get_encoding, get_delimiter
from files_utils import read_csv, process_data, write_json
from logging_utils import setup_logging

if __name__ == "__main__":
    try:
        setup_logging()
        config = read_config()
        csv_file_path = config.get('path', 'csv_file')
        json_file_path = config.get('path', 'json_file')

        header, csv_data = read_csv(csv_file_path, get_delimiter(config))
        json_data = process_data(header, csv_data)
        write_json(json_data, json_file_path, get_encoding(config))

        logging.info("Conversion completed successfully.")
    except Exception as e:
        logging.error(f'An error occurred: {e}')
