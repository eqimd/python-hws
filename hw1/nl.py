from sys import argv, stdin

LEFT_TAB_SIZE = 6
INNER_TAB_SIZE = 2
FORMAT_STR = '{:>' + str(LEFT_TAB_SIZE) + '}' + ' '*INNER_TAB_SIZE + '{}'

def main():
    fileNl = None

    if len(argv) == 1:
        fileNl = stdin
    else:
        fileNl = open(argv[1], 'r')

    for idx, line in enumerate(fileNl):
        print(FORMAT_STR.format(idx+1, line.strip()))

    fileNl.close()    


if __name__ == '__main__':
    main()