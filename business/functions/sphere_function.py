from business.functions.fitness_function import FitnessFunction


class SphereFunction(FitnessFunction):

    def __init__(self):
        super(SphereFunction, self).__init__('Sphere', (-100.0, 100.0), (50.0, 100.0))

    @staticmethod
    def run(x):
        return (x ** 2).sum()
