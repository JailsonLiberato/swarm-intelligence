from business.services.service import Service
from util.constants import Constants
from model.food_source import FoodSource
from business.functions.fitness_function import FitnessFunction
import numpy as np


class FoodSourceService(Service):

    def initialize_food_source(self, fitness_function: FitnessFunction):
        food_sources = []
        for i in range(Constants.N_FOOD_SOURCE):
            position = self.__generate_initial_position(fitness_function)
            food_source = FoodSource(position)
            food_sources.append(food_source)
        return food_sources

    @staticmethod
    def __generate_initial_position(fitness_function: FitnessFunction):
        position = []
        min_value = fitness_function.min_initialization
        max_value = fitness_function.max_initialization
        for _ in range(Constants.N_DIMENSIONS):
            random_value = np.random.uniform(0, 1, size=(1, 1))
            x = min_value + random_value * (max_value - min_value)
            position.append(x)
        return position
