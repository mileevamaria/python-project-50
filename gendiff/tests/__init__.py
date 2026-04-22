import os

from gendiff.tools import load_json, load_yaml

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(TESTS_DIR, 'test_data')


def read_json_file(filename: str) -> dict:
    filepath = os.path.join(TEST_DATA_DIR, filename)
    return load_json(filepath)


def read_txt_file(filename: str) -> str:
    filepath = os.path.join(TEST_DATA_DIR, filename)
    with open(filepath, 'r') as f:
        return f.read()


def read_yaml_file(filename: str) -> dict:
    filepath = os.path.join(TEST_DATA_DIR, filename)
    return load_yaml(filepath)


__all__ = (
    'read_json_file',
    'read_txt_file',
    'read_yaml_file',
)
