from gendiff import generate_diff
from gendiff.tests import read_txt_file, read_yaml_file


def test_stylish():
    f1 = read_yaml_file('a.yaml')
    f2 = read_yaml_file('b.yaml')
    expected = read_txt_file('expected_stylish.txt')
    result = generate_diff(f1, f2, format_name='stylish')
    assert result == expected


def test_plain():
    f1 = read_yaml_file('a.yaml')
    f2 = read_yaml_file('b.yaml')
    expected = read_txt_file('expected_plain.txt')
    result = generate_diff(f1, f2, format_name='plain')
    assert result.strip() == expected


def test_json():
    f1 = read_yaml_file('a.yaml')
    f2 = read_yaml_file('b.yaml')
    expected = read_txt_file('expected_json.json')
    result = generate_diff(f1, f2, format_name='json')
    assert result == expected
