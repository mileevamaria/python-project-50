import os

from gendiff import load_json, load_yaml

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DATA_PATH = os.path.join(TEST_DIR, 'test_data/input')
OUTPUT_DATA_PATH = os.path.join(TEST_DIR, 'test_data/output')


def read_json_file(filename: str) -> dict:
    filepath = os.path.join(INPUT_DATA_PATH, filename)
    return load_json(filepath)


def read_txt_file(filename: str) -> str:
    filepath = os.path.join(OUTPUT_DATA_PATH, filename)
    with open(filepath, 'r') as f:
        return f.read()


def read_yaml_file(filename: str) -> dict:
    filepath = os.path.join(INPUT_DATA_PATH, filename)
    return load_yaml(filepath)


__all__ = (
    'read_json_file',
    'read_txt_file',
    'read_yaml_file',
)
