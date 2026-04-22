from gendiff import generate_diff, parse_command
from gendiff.tools import load_json, load_yaml


def main():
    file_path1, file_path2, format = parse_command()
    load_func = load_json if file_path1.endswith('.json') else load_yaml
    data1, data2 = load_func(file_path1), load_func(file_path2)
    diff = generate_diff(data1, data2, format)
    print(diff)


if __name__ == '__main__':
    main()
