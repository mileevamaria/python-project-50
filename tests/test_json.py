import os

from gendiff import generate_diff
from tests import TEST_DATA_DIR, read_txt_file


def test_stylish():
    file_path1 = os.path.join(TEST_DATA_DIR, 'a.json')
    file_path2 = os.path.join(TEST_DATA_DIR, 'b.json')
    expected = read_txt_file('expected_stylish.txt')
    result = generate_diff(file_path1, file_path2, format_name='stylish')
    assert result == expected

    
def test_plain():
    file_path1 = os.path.join(TEST_DATA_DIR, 'a.json')
    file_path2 = os.path.join(TEST_DATA_DIR, 'b.json')
    expected = read_txt_file('expected_plain.txt')
    result = generate_diff(file_path1, file_path2, format_name='plain')
    assert result.strip() == expected


def test_json():
    file_path1 = os.path.join(TEST_DATA_DIR, 'a.json')
    file_path2 = os.path.join(TEST_DATA_DIR, 'b.json')
    expected = read_txt_file('expected_json.json')
    result = generate_diff(file_path1, file_path2, format_name='json')
    assert result == expected
