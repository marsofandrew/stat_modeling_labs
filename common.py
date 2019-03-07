#!/bin/python

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
        for j in range(len(data_set) - i):
            iteration += (data_set[j] - mean) * (data_set[j + i] - mean)
        correlation.append(iteration / accumulation)
    return correlation


def show_density(data_set, parts=100):
    plot.hist(data_set, parts, density=True)
    plot.show()
    plot.hist(data_set, parts, cumulative=True)
    plot.show()


def stirling(a, b):
    if abs(a-b)<1e-8:
        return 1
    if abs(b)<1e-8:
        return 0
    return b * stirling(a - 1, b) + stirling(a - 1, b - 1)
