from gendiff import generate_diff
from gendiff.tests import read_json_file, read_txt_file


def test_equal_json():
    f1 = read_json_file('equal_1.json')
    f2 = read_json_file('equal_2.json')
    result = generate_diff(f1, f2)
    expected = read_txt_file('equal.txt')
    assert result == expected


def test_value_changed():
    f1 = read_json_file('value_changed_1.json')
    f2 = read_json_file('value_changed_2.json')
    result = generate_diff(f1, f2)
    expected = read_txt_file('value_changed.txt')
    assert result == expected


def test_removed_key():
    f1 = read_json_file('removed_key_1.json')
    f2 = read_json_file('removed_key_2.json')
    result = generate_diff(f1, f2)
    expected = read_txt_file('removed_key.txt')
    assert result == expected


def test_added_key():
    f1 = read_json_file('added_key_1.json')
    f2 = read_json_file('added_key_2.json')
    result = generate_diff(f1, f2)
    expected = read_txt_file('added_key.txt')
    assert result == expected


def test_multiple_changed_keys():
    f1 = read_json_file('multiple_changed_keys_1.json')
    f2 = read_json_file('multiple_changed_keys_2.json')
    result = generate_diff(f1, f2)
    expected = read_txt_file('multiple_changed_keys.txt')
    assert result == expected


def test_boolean_and_none():
    f1 = read_json_file('boolean_and_none_1.json')
    f2 = read_json_file('boolean_and_none_2.json')
    result = generate_diff(f1, f2)
    expected = read_txt_file('boolean_and_none.txt')
    assert result == expected


def test_empty_files():
    f1 = read_json_file('empty_1.json')
    f2 = read_json_file('empty_2.json')
    result = generate_diff(f1, f2)
    expected = read_txt_file('empty.txt')
    assert result == expected
