import csv
import json


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
