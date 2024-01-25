import configparser
import logging

CONFIG_FILE = '../../config.ini'


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
