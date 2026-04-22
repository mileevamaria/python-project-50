import argparse
import json

import yaml

from .format import stylish


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
    data1: dict, 
    data2: dict, 
    format_name: str = 'stylish',
):
    diff = create_diff_data(data1, data2)
    match format_name:
        case 'stylish':
            return stylish(diff)


def parse_command() -> tuple[dict, dict]:
    parser = argparse.ArgumentParser(
        prog='gendiff', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output')
    args = vars(parser.parse_args())

    # json
    if args['first_file'].endswith('.json'):
        load_func = load_json
    # yml, yaml
    else:
        load_func = load_yaml

    data1 = load_func(args['first_file'])
    data2 = load_func(args['second_file'])
    return data1, data2
