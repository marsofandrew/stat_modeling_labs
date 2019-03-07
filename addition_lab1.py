#!/bin/python
import numpy as np
import math
import common

M = 2
T = 6
N = 20


def is_have_all_values(data, m):
    data_list = data.tolist()
    for i in range(2 ** m):
        if data_list.count(i) <= 0:
            return False
    return True


def count_v(data, m, t):
    v = dict()
    for size in range(m ** 2, t + 1):
        v[size] = 0
        for i in range(len(data) - size + 1):
            if is_have_all_values(data[i:i + size], m):
                v[size] += 1
    return v


def count_p(m, t):
    p = dict()
    d = t - 1
    for i in range(2 ** m, t):
        p[i] = math.factorial(d) / math.pow(d, i) * common.stirling(i - 1, d - 1)
    p[t] = 1 - math.factorial(d) / math.pow(d, t - 1) * common.stirling(t - 1, d)
    return p


def main():
    data_set = np.random.randint(0, 2 ** M, N)
    v = count_v(data_set, M, T)
    print(v)
    p = count_p(M, T)
    print(p)
    sum_v = sum(v.values())
    print(sum_v)
    hi_2 = 0
    for i in range(2 ** M, T + 1):
        hi_2 += ((v[i] - sum_v * p[i]) ** 2) / (p[i] * sum_v)
    print("result hi_2 = {}".format(hi_2))


if __name__ == '__main__':
    main()
