from business.services.service import Service
from business.functions.fitness_function import FitnessFunction


class ArtificialBeeColonyService(Service):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fitness_function = fitness_function
        self.__fitness_values = []
        self.__execute()

    def __execute(self):
        pass

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values

