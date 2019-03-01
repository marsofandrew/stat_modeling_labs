#!/bin/python

from lab_2_random_generators import *
import common

uniform_generator = UniformDistributionIntGenerator(0, 1000)
binomial_generator = BinomialDistributionGenerator(10, 0.5)
data = []
for i in range(1_000_000):
    data.append(binomial_generator.generate())
common.plot.hist(data,100, histtype='step', density=True)
common.plot.show()
