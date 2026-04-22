from gendiff import generate_diff, parse_command


def main():
    file_path1, file_path2, format = parse_command()
    diff = generate_diff(file_path1, file_path2, format)
    print(diff)


if __name__ == '__main__':
    main()
