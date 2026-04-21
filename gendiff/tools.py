import argparse
import json

import yaml


def load_json(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)
    

def load_yaml(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)
    

def generate_diff(data1: dict, data2: dict) -> str:
    result = '{\n'
    # Unique sorted keys
    keys = [*list(data1.keys()), *list(data2.keys())]
    keys = sorted(list(set(keys)))
    for key in keys:
        if key in data2 and key in data1:
            if data1[key] == data2[key]:
                result += f'    {key}: {data1[key]}\n'
            else:
                result += f'  - {key}: {data1[key]}\n'
                result += f'  + {key}: {data2[key]}\n'
        elif key not in data2:
            result += f'  - {key}: {data1[key]}\n'
        else:
            result += f'  + {key}: {data2[key]}\n'
    result += '}'
    return result


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
