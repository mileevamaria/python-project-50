from gendiff import generate_diff, parse_command


def main():
    data1, data2 = parse_command()
    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == '__main__':
    main()
