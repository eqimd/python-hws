from sys import argv, stdin

STAT_TAB_SIZE = 8
FORMAT_STR = ('{:>' + str(STAT_TAB_SIZE) + '}')*3 + ' {}'


def calc_wc(file):
    byte_cnt = 0
    word_cnt = 0
    line_cnt = 0

    for line in file:
        line_cnt += 1
        byte_cnt += len(line)

        splitted = line.split()
        word_cnt += len(splitted)

    return (line_cnt, word_cnt, byte_cnt)


def main():
    total_byte_cnt = 0
    total_word_cnt = 0
    total_line_cnt = 0

    filenames = argv[1:]

    if len(filenames) == 0:
        line_cnt, word_cnt, byte_cnt = calc_wc(stdin)
        print(FORMAT_STR.format(line_cnt, word_cnt, byte_cnt, ''))
        return

    for fn in filenames:
        f = open(fn, 'r')

        line_cnt, word_cnt, byte_cnt = calc_wc(f)
        print(FORMAT_STR.format(line_cnt, word_cnt, byte_cnt, fn))

        total_line_cnt += line_cnt
        total_word_cnt += word_cnt
        total_byte_cnt += byte_cnt

        f.close()

    if len(filenames) > 1:
        print(FORMAT_STR.format(total_line_cnt, total_word_cnt, total_byte_cnt, 'total'))

if __name__ == '__main__':
    main()