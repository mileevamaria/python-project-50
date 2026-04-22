import argparse
import json

import yaml

from gendiff.formatеrs import jsonify, plain, stylish


def load_json(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)
    

def load_yaml(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def create_diff_data(data1: dict, data2: dict):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    for key in keys:
        value1, value2 = data1.get(key), data2.get(key)
        if key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': value2,
            })
        elif key not in data2:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': value1,
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': create_diff_data(value1, value2),
            })
        elif value1 == value2:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': value1,
            })
        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': value1,
                'new_value': value2,
            })
    return diff


def generate_diff(
    file_path1: str, 
    file_path2: str, 
    format_name: str | None = 'stylish',
):
    load_func = load_json if file_path1.endswith('.json') else load_yaml
    data1, data2 = load_func(file_path1), load_func(file_path2)  
    diff = create_diff_data(data1, data2)
    match format_name:
        case 'plain':
            return plain(diff)
        case 'json':
            return jsonify(diff)
        case _:
            return stylish(diff)


def parse_command() -> tuple[str, str, str]:
    parser = argparse.ArgumentParser(
        prog='gendiff', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output')
    first_file, second_file, format = vars(parser.parse_args()).values()
    return first_file, second_file, format
