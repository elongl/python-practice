def main():
    print("Please enter a file's name in the working directory.")
    while True:
        filename = input()
        try:
            with open(filename, 'r') as file:
                lines = file.read().splitlines()
            new_lines = map(lambda line: f'Elon {line} Gliksberg\n', lines)
            with open('output.txt', 'w') as file:
                file.writelines(new_lines)
            break
        except FileNotFoundError:
            print("Please make sure you entered a valid file name.")


if __name__ == '__main__':
    main()
