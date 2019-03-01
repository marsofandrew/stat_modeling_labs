#!/bin/python

MAX_DATA_SIZE = 1e4
EXPECTED_MEAN = 0.5
EXPECTED_DISPERSION = 0.08333

from common import *
from matplotlib import pyplot as plot





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
