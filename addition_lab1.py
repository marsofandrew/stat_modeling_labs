#!/bin/python

DATA_SET_SIZE = 10_000
import common
from matplotlib import pyplot as plot


def main():
    data_set = []
    for i in range(2):
        data_set.append(common.create_data_set(DATA_SET_SIZE))
    for i in range(len(data_set[0])):
        if data_set[0][i] > data_set[1][i]:
            data_set[0][i], data_set[1][i] = data_set[1][i], data_set[0][i]



if __name__ == '__main__':
    main()
