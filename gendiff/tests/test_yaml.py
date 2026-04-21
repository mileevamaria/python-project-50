from gendiff import generate_diff
from gendiff.tests import read_txt_file, read_yaml_file


def test_equal_json():
    f1 = read_yaml_file('equal_1.yaml')
    f2 = read_yaml_file('equal_2.yaml')
    result = generate_diff(f1, f2)
    expected = read_txt_file('equal.txt')
    assert result == expected


def test_value_changed():
    f1 = read_yaml_file('value_changed_1.yaml')
    f2 = read_yaml_file('value_changed_2.yaml')
    result = generate_diff(f1, f2)
    expected = read_txt_file('value_changed.txt')
    assert result == expected


def test_removed_key():
    f1 = read_yaml_file('removed_key_1.yaml')
    f2 = read_yaml_file('removed_key_2.yaml')
    result = generate_diff(f1, f2)
    expected = read_txt_file('removed_key.txt')
    assert result == expected


def test_added_key():
    f1 = read_yaml_file('added_key_1.yaml')
    f2 = read_yaml_file('added_key_2.yaml')
    result = generate_diff(f1, f2)
    expected = read_txt_file('added_key.txt')
    assert result == expected


def test_multiple_changed_keys():
    f1 = read_yaml_file('multiple_changed_keys_1.yaml')
    f2 = read_yaml_file('multiple_changed_keys_2.yaml')
    result = generate_diff(f1, f2)
    expected = read_txt_file('multiple_changed_keys.txt')
    assert result == expected


def test_boolean_and_none():
    f1 = read_yaml_file('boolean_and_none_1.yaml')
    f2 = read_yaml_file('boolean_and_none_2.yaml')
    result = generate_diff(f1, f2)
    expected = read_txt_file('boolean_and_none.txt')
    assert result == expected


def test_empty_files():
    f1 = read_yaml_file('empty_1.yaml')
    f2 = read_yaml_file('empty_2.yaml')
    result = generate_diff(f1, f2)
    expected = read_txt_file('empty.txt')
    assert result == expected
