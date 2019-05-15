from business.functions.fitness_function import FitnessFunction


class RosenbrockFunction(FitnessFunction):

    def __init__(self):
        super(RosenbrockFunction, self).__init__('Rosenbrock', (-30.0, 30.0), (15.0, 30.0))

    @staticmethod
    def run(x):
        a = x[1:] - (x[:-1] ** 2)
        b = x[:1] - 1
        y = 100 * (a ** 2) + (b ** 2)
        return y.sum()
