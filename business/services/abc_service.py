from business.services.service import Service
from business.functions.fitness_function import FitnessFunction
from business.services.food_source_service import FoodSourceService


class ArtificialBeeColonyService(Service):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fitness_function = fitness_function
        self.__fitness_values = []
        self.__food_source_service = FoodSourceService()
        self.__food_sources = self.__food_source_service.initialize_food_source(self.fitness_values)
        self.__execute()

    def __execute(self):
        pass

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values

