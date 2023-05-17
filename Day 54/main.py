import time
import random

st = time.time()
nlist = random.sample(range(100000000), 10000000)
print(f"list generation speed: {time.time() - st}")

st1 = time.time()
num_list = sorted(nlist)
print(f"nlogn sort run speed: {time.time() - st1}")

find_num = random.choice(num_list)


def speed_decorator(func):
    def speed():
        start_time = time.time()
        func(find_num, num_list)
        print(func.__name__, "run speed: ", time.time() - start_time)
    return speed


@speed_decorator
def linear_search(find_num: int, num_list: list):
    for num in num_list:
        if num == find_num:
            break


@speed_decorator
def binary_search(find_num: int, num_list: list):
    start = 0
    end = len(num_list) - 1
    while start < end:
        middle = (start + end) // 2
        curr_num = num_list[middle]
        if curr_num == find_num:
            break
        elif curr_num > find_num:
            end = middle - 1
        else:
            start = middle + 1


linear_search()
binary_search()
