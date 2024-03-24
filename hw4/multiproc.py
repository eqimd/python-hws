from multiprocessing import Queue, Pipe, Process
from multiprocessing.connection import Connection
from codecs import encode
from time import sleep
from datetime import datetime


SLEEP_LOWER_SEC = 5


def func_proc_lower(queue: Queue, read_pipe: Connection):
    while not read_pipe.closed:
        s = str(read_pipe.recv()).lower()

        sleep(SLEEP_LOWER_SEC)

        queue.put(s)


def func_proc_rot13(queue: Queue, write_pipe: Connection):
    while not write_pipe.closed:
        s = str(queue.get())
        s = encode(s, 'rot_13')

        write_pipe.send(s)


def main():
    msg_queue = Queue()
    rot_read_pipe, rot_write_pipe = Pipe()
    lower_read_pipe, lower_write_pipe = Pipe()

    proc_lower = Process(target=func_proc_lower, args=(msg_queue, lower_read_pipe,))
    proc_rot13 = Process(target=func_proc_rot13, args=(msg_queue, rot_write_pipe,))

    proc_lower.start()
    proc_rot13.start()

    while True:
        s = input()

        print(f'[{datetime.now()}] Got new message from stdin: {s}')

        lower_write_pipe.send(s)
        print(f'[{datetime.now()}] Sent message to lower')
        s = rot_read_pipe.recv()

        print(f'[{datetime.now()}] Got processed message: {s}')


if __name__ == '__main__':
    main()
