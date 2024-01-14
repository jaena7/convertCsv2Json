import csv
import json
import configparser
import logging

CONFIG_FILE = 'config.ini'

logging.basicConfig(level=logging.INFO)

def read_config():
    config_parser = configparser.ConfigParser()
    try:
        config_parser.read(CONFIG_FILE, encoding='utf-8')
        return config_parser
    except Exception as e:
        logging.error(f'Error reading config file: {e}')
        raise SystemExit()


def get_delimiter(configuration):
    delimiter = configuration.get('setup', 'delimiter')
    logging.info(f'delimiter: {delimiter}')
    return delimiter


def get_encoding(configuration):
    encoding = configuration.get('setup', 'encoding')
    logging.info(f'encoding: {encoding}')
    return encoding


def read_csv(csv_file, delimiter):
    with open(csv_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        header = next(csv_reader)
        csv_data = list(csv_reader)
        return header, csv_data


def process_data(csv_header, csv_data):
    # Define a mapping for boolean values
    boolean_mapping = {'true': True, 'false': False, 'yes': True, 'no': False, 'ano': True, 'ne': False, None: False}

    json_data = []
    for row in csv_data:
        row_dict = {}
        for i in range(len(csv_header)):
            # Check if the header corresponds to a boolean column
            if csv_header[i].lower() in boolean_mapping:
                # Map the string value to a boolean
                row_dict[csv_header[i].strip()] = boolean_mapping[row[i].strip().lower()]
            else:
                row_dict[csv_header[i].strip()] = row[i].strip()

        json_data.append(row_dict)

    # Convert the entire JSON data to a string
    json_data_str = json.dumps(json_data)

    # Replace boolean strings with actual boolean values
    for key, value in boolean_mapping.items():
        json_data_str = json_data_str.replace(f'"{key}"', json.dumps(value))

    # Load the modified string back to JSON format
    json_data_json = json.loads(json_data_str)

    return json_data_json


def write_json(json_data, json_file, encoding):
    with open(json_file, "w", encoding=encoding) as json_file:
        json_file.write(json.dumps(json_data, indent=4))


if __name__ == "__main__":
    try:
        config = read_config()
        csv_file_path = config.get('path', 'csv_file')
        json_file_path = config.get('path', 'json_file')

        header, csv_data = read_csv(csv_file_path, get_delimiter(config))
        json_data = process_data(header, csv_data)
        write_json(json_data, json_file_path, get_encoding(config))

        logging.info("Conversion completed successfully.")
    except Exception as e:
        logging.error(f'An error occurred: {e}')
