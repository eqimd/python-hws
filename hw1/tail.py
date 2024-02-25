from collections import deque
from sys import argv, stdin

FILE_TAIL_LEN = 10
STDIN_TAIL_LEN = 17

HEADER_FORMAT_STRING = '==> {} <=='


def print_tail(file, tail_len):
    dq = deque(maxlen=tail_len)

    for line in file:
        dq.append(line.strip())

    for e in dq:
        print(e)


def main():
    filenames = argv[1:]

    if len(filenames) == 0:
        print_tail(stdin, STDIN_TAIL_LEN)
        return
    elif len(filenames) == 1:
        f = open(filenames[0], 'r')
        print_tail(f, FILE_TAIL_LEN)

        f.close()
        return
    
    fn = filenames[0]
    f = open(fn, 'r')

    print(HEADER_FORMAT_STRING.format(fn))
    print_tail(f, FILE_TAIL_LEN)

    f.close()
    
    for fn in filenames[1:]:
        f = open(fn, 'r')

        print()
        print(HEADER_FORMAT_STRING.format(fn))
        print_tail(f, FILE_TAIL_LEN)

        f.close()


if __name__ == '__main__':
    main()