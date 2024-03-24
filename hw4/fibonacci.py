from sys import argv
from datetime import datetime, timedelta
from threading import Thread
from multiprocessing import Process


CALC_COUNT = 10


def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def calc_fibonacci_sync(n: int) -> timedelta:
    begin_time = datetime.now()

    for _ in range(CALC_COUNT):
        fibonacci(n)

    return datetime.now() - begin_time


def calc_fibonacci_threads(n: int) -> timedelta:
    begin_time = datetime.now()

    calc_threads = [Thread(target=fibonacci, args=(n,)) for _ in range(CALC_COUNT)]

    for t in calc_threads:
        t.start()

    for t in calc_threads:
        t.join()

    return datetime.now() - begin_time


def calc_fibonacci_procs(n: int) -> timedelta:
    begin_time = datetime.now()

    calc_threads = [Process(target=fibonacci, args=(n,)) for _ in range(CALC_COUNT)]

    for t in calc_threads:
        t.start()

    for t in calc_threads:
        t.join()

    return datetime.now() - begin_time


def main():
    method = argv[1]
    n = int(argv[2])

    calc_time = 0

    match method:
        case 'sync':
            calc_time = calc_fibonacci_sync(n)
        case 'threads':
            calc_time = calc_fibonacci_threads(n)
        case 'procs':
            calc_time = calc_fibonacci_procs(n)
        case _:
            print('unknown method')
            return
        

    print(f'calculation time for n={n} is {calc_time}')


if __name__ == '__main__':
    main()
