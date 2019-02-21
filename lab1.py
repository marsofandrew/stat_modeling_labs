#!/bin/python

MAX_DATA_SIZE = 10e6
EXPECTED_MEAN = 0.5
EXPECTED_DISPERSION = 0.08333

import random
import numpy


def create_data_set(size):
    dataset = list()
    for i in range(size):
        dataset.append(random.random())
    return dataset


def count_mean(data_set):
    return numpy.mean(data_set)


def count_dispersion(data_set, mean=None):
    if mean is None:
        mean = count_mean(data_set)
    if len(data_set) == 0:
        raise AttributeError("data_set should has data")
    dispersion = 0
    for x in data_set:
        dispersion += (x - mean) ** 2
    return dispersion / len(data_set)


def count_auto_correlation(data_set, mean=None):
    pass


def proceed_step(data_size):
    data = create_data_set(data_size)
    mean = count_mean(data)
    dispersion = count_dispersion(data, mean)
    print("data size: {}; mean: {}; mean difference: {}; dispersion: {}; dispersion difference: {}".format(
        data_size, mean, mean - EXPECTED_MEAN, dispersion, dispersion - EXPECTED_DISPERSION))
    return data, mean, dispersion


def main():
    print("\n===== lab 1 is started =====\n")
    size_of_data = 10
    while size_of_data <= MAX_DATA_SIZE:
        data, mean, dispersion = proceed_step(size_of_data)
        size_of_data *= 10

    print("\n===== lab 1 is finished =====")


if __name__ == '__main__':
    main()
