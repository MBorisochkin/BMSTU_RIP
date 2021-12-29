from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:
    """Контекстный менеджер на основе класса"""
    def __init__(self):
        self.start_time = None
        self.finish_time = None

    def __enter__(self):
        self.start_time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = time()
        print("Время: {}".format(self.finish_time - self.start_time))


@contextmanager
def cm_timer_2():
    """Контекстный менеджер на основе библиотеки contextlib"""
    start_time = time()
    yield
    finish_time = time()
    print("Время: {}".format(finish_time - start_time))


if __name__ == '__main__':
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)
