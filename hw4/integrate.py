import math
import os

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime
from sys import argv, stdout


def calc_f(args):
    f = args[0]
    n_iter = args[1]
    arg = args[2]
    step = args[3]

    print(f'[{datetime.now()}] started task {n_iter} with arg={arg}')

    return f(arg) * step


def integrate_threads(f, a, b, *, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_iter

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        args = [(f, i, a + i*step, step) for i in range(n_iter)]

        calculated = executor.map(calc_f, args)

        return sum(calculated)


def integrate_procs(f, a, b, *, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_iter

    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        args = [(f, i, a + i*step, step) for i in range(n_iter)]

        calculated = executor.map(calc_f, args)

        return sum(calculated)


def main():
    method = argv[1]

    cpus = os.cpu_count() * 2

    n_iter = 10000

    # List of calculation time with pair (n_jobs, calculation time)
    calc_times = []

    match method:
        case 'threads':
            for n_jobs in range (1, cpus+1):
                print(f'started calculating on threads with n_jobs={n_jobs}')

                begin_time = datetime.now()

                integrate_threads(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=n_iter)

                calc_time = datetime.now() - begin_time
                calc_times.append((n_jobs, calc_time))


        case 'procs':
            for n_jobs in range (1, cpus+1):
                print(f'started calculating on processes with n_jobs={n_jobs}')

                begin_time = datetime.now()

                integrate_procs(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=n_iter)

                calc_time = datetime.now() - begin_time
                calc_times.append((n_jobs, calc_time))
        
        case _:
            print('unknown method')

            return

    stdout.flush()

    print('calculaction times:')
    for n_jobs, calc_time in calc_times:
        print(f'n_jobs={n_jobs}, calc_time={calc_time}')


if __name__ == '__main__':
    main()
