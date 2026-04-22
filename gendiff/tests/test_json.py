from gendiff import generate_diff
from gendiff.tests import read_json_file, read_txt_file


def test_stylish():
    f1 = read_json_file('a.json')
    f2 = read_json_file('b.json')
    expected = read_txt_file('expected_stylish.txt')
    result = generate_diff(f1, f2, format_name='stylish')
    assert result == expected


def test_plain():
    f1 = read_json_file('a.json')
    f2 = read_json_file('b.json')
    expected = read_txt_file('expected_plain.txt')
    result = generate_diff(f1, f2, format_name='plain')
    assert result.strip() == expected


def test_json():
    f1 = read_json_file('a.json')
    f2 = read_json_file('b.json')
    expected = read_txt_file('expected_json.json')
    result = generate_diff(f1, f2, format_name='json')
    assert result == expected
