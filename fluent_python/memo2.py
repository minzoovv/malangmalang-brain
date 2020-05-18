from uuid import uuid4
from random import randint
import time


def check_time(original_fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_fun(*args, **kwargs)
        print('Working time: ', time.time() - start)
        return result
    return wrapper


@check_time
def for_in_with_list(a: list, val: str):
    if val in a:
        return


@check_time
def for_in_with_set(a: set, val: str):
    if val in a :
        return


if __name__ == '__main__':
    list_a = list([uuid4().hex for _ in range(10000)])
    set_a = set(list_a)
    idx = randint(0, len(list_a))
    print(idx)
    for_in_with_list(list_a, list_a[idx])
    for_in_with_set(set_a, list_a[idx])

