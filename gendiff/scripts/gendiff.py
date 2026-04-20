import argparse
import json

DATA_FILE_1_PATH = '../data/file1.json'
DATA_FILE_2_PATH = '../data/file2.json'


def parse(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = vars(parser.parse_args())
    print(parse(args['first_file']))
    print(parse(args['second_file']))


if __name__ == '__main__':
    main()
