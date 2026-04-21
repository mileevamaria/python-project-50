import argparse

from gendiff import generate_diff, load_json


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff', 
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = vars(parser.parse_args())
    data1, data2 = load_json(args['first_file']), load_json(args['second_file'])
    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == '__main__':
    main()
