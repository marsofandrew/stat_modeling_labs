#!/bin/python

import random
import numpy
import math
from abc import ABC, abstractmethod


class DistributionGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class UniformDistributionIntGenerator(DistributionGenerator):
    minimum = 0
    maximum = 0

    def __init__(self, minimum=0, maximum=100):
        if minimum >= maximum:
            raise ValueError("minimum should be less or than maximum")
        self.minimum = minimum
        self.maximum = maximum

    def generate(self):
        return int((self.maximum - self.minimum + 1) * random.random() + self.minimum)


class BinomialDistributionGenerator(DistributionGenerator):
    n = -1
    p = -1

    def __init__(self, n, p):
        if p > 1:
            raise ValueError("p must be less or equal 1")
        self.n = n
        self.p = p

    def generate(self):
        return int(numpy.random.normal(self.n * self.p, math.sqrt(self.n * self.p * (1 - self.p))) + 0.5)


class GeometricDistributionGenerator(DistributionGenerator):
    p = -1

    def __init__(self, p):
        if p > 1:
            raise ValueError("p must be less or equal 1")
        self.p = p

    def generate(self):
        return int(math.log(random.random(), math.e) / math.log((1 - self.p), math.e)) + 1
