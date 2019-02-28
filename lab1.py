#!/bin/python

MAX_DATA_SIZE = 1e4
EXPECTED_MEAN = 0.5
EXPECTED_DISPERSION = 0.08333

import random
import numpy
from matplotlib import pyplot as plot


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
    if mean is None:
        mean = count_mean(data_set)
    accumulation = 0
    for x in data_set:
        accumulation += (x - mean) ** 2

    correlation = [None]
    for i in range(1, len(data_set)):
        iteration = 0
        for j in range(len(data_set)-i):
            iteration += (data_set[j] - mean) * (data_set[j+i] - mean)
        correlation.append( iteration / accumulation)
    return correlation


def show_density(data_set, parts=100):
    plot.hist(data_set, parts, density=True)
    plot.show()
    plot.hist(data_set, parts, cumulative=True)
    plot.show()


def proceed_step(data_size):
    data = create_data_set(data_size)
    mean = count_mean(data)
    dispersion = count_dispersion(data, mean)
    print("|%13d|%-13f|%-13f|%-13f|%-17f|" % (
        data_size, float(mean), float(mean - EXPECTED_MEAN), float(dispersion),
        float(dispersion - EXPECTED_DISPERSION)))
    return data, mean, dispersion


def main():
    print("\n===== lab 1 is started =====\n")
    size_of_data = 10

    print("| data size   | mean        | mean diff   | dispersion  | dispersion diff |")
    while size_of_data <= MAX_DATA_SIZE:
        data, mean, dispersion = proceed_step(size_of_data)
        size_of_data *= 10
        k = count_auto_correlation(data, mean)
        show_density(data, 10)
        plot.plot(k)
        plot.show()

    print("\n===== lab 1 is finished =====")


if __name__ == '__main__':
    main()
