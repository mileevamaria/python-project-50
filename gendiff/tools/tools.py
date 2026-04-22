import argparse
import json

import yaml

from .formatter import Formatter


def load_json(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)
    

def load_yaml(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)
    

def get_unique_sorted_keys(data1: dict, data2: dict) -> list:
    keys = [*list(data1.keys()), *list(data2.keys())]
    return sorted(list(set(keys)))

    
def generate_diff(data1: dict, data2: dict, format_name='stylish'):
    diff = {}
    keys = get_unique_sorted_keys(data1, data2)
    for key in keys:
        if key in data2 and key in data1:
            diff[key] = {
                'data1': data1[key],
                'data2': data2[key],
            }
            if data1[key] == data2[key]:
                diff[key]['status'] = 'same'
            else:
                diff[key]['status'] = 'changed'
        elif key not in data2:
            diff[key] = {
                'status': 'removed',
                'data1': data1[key],
            }
            
        else:
            diff[key] = {
                'status': 'added',
                'data2': data2[key],
            }
    formatter_func = getattr(Formatter, format_name)
    return formatter_func(diff)


def parse_command() -> tuple[dict, dict]:
    parser = argparse.ArgumentParser(
        prog='gendiff', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
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
