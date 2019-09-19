import numpy as np
import timeit
import pandas as pd
import matplotlib.pyplot as plt


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped()


def max_sub_array_brute(ar):
    max_sub_array = ar[0]
    for i in range(len(ar)):
        sub_array_value = ar[i]
        start = i + 1
        for k in range(start, len(ar)):
            sub_array_value = sub_array_value + ar[k]
            if max_sub_array < sub_array_value:
                max_sub_array = sub_array_value
    return max_sub_array


def max_sub_array_linear(ar):
    max_ending = ar[0]
    max_so_far = ar[0]
    for i in range(1, len(ar)):
        if max_ending + ar[i] > ar[i]:
            max_ending += ar[i]
        else:
            max_ending = ar[i]
        if max_so_far < max_ending:
            max_so_far = max_ending
    return max_ending


def create_random_array(number_of_elements):
    return np.random.randint(-1000, 1000, number_of_elements)


def linear_time(start, stop, by, file='linear_times.txt'):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import max_sub_array_linear
from __main__ import wrapper
import numpy as np'''
    TEST_CODE = '''
a = create_random_array(a_size)
max_sub_array_linear(a)'''
    times = list()
    for i in range(start, stop, by):
        time = timeit.timeit(setup=SETUP_CODE,
                             stmt=TEST_CODE.replace('a_size', str(i)),
                             number=100)
        times.append(time)
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


def brute_time(start, stop, by, file='brute_times.txt'):
    SETUP_CODE = '''
from __main__ import create_random_array
from __main__ import max_sub_array_brute
from __main__ import wrapper
import numpy as np'''
    TEST_CODE = '''
a = create_random_array(a_size)
max_sub_array_brute(a)'''
    times = list()
    for i in range(start, stop, by):
        time = timeit.timeit(setup=SETUP_CODE,
                             stmt=TEST_CODE.replace('a_size', str(i)),
                             number=100)
        print(i)
        times.append(time)
    with open(file, "w+") as file:
        for t in times:
            file.write('%s\n' % t)
    return times


if __name__ == '__main__':
    start = 10
    stop = 110
    by = 10
    lin = linear_time(start, stop, by)
    bru = brute_time(start, stop, by)
    data = pd.DataFrame({'x': range(start, stop, by), 'linear': lin, 'brute': bru})
    plt.plot('x', 'linear', data=data)
    plt.plot('x', 'brute', data=data)
    plt.legend()
    plt.show()

