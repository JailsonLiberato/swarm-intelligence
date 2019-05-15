from business.functions.fitness_function import FitnessFunction
import numpy as np


class RastringinFunction(FitnessFunction):

    def __init__(self):
        super(RastringinFunction, self).__init__('Rastringin', (-5.12, 5.12), (2.56, 5.12))

    @staticmethod
    def run(x):
        y = (x ** 2) - 10 * np.cos(2.0 * np.pi * x) + 10
        return y.sum()
