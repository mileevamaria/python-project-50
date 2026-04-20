import json


def _parse_json(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)
    

def generate_diff(file_path1: str, file_path2: str) -> str:
    result = '{\n'
    data1, data2 = _parse_json(file_path1), _parse_json(file_path2)
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
