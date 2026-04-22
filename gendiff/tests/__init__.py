import os

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(TESTS_DIR, 'test_data')


def read_txt_file(filename: str) -> str:
    filepath = os.path.join(TEST_DATA_DIR, filename)
    with open(filepath, 'r') as f:
        return f.read()


__all__ = (
    'TEST_DATA_DIR',
    'read_txt_file'
)
