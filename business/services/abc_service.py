from business.services.service import Service
from business.functions.fitness_function import FitnessFunction


class ArtificialBeeColonyService(Service):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fitness_function = fitness_function
        self.__execute()

    def __execute(self):
        pass

