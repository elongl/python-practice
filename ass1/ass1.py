print("Please enter a file's name in the working directory.")
while True:
    filename = input()
    try:
        file = open(filename, 'r')
        lines = file.read().splitlines()
        file.close()
        file = open('output.txt', 'w')
        new_lines = map(lambda line: 'Elon %s Gliksberg\n' % line, lines)
        file.writelines(new_lines)
        file.close()
        break
    except FileNotFoundError:
        print("Please make sure you entered a valid file name.")
