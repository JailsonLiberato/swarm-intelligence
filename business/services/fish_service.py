from business.services.service import Service
from util.constants import Constants
from business.functions.fitness_function import FitnessFunction
import numpy as np
from model.fish import Fish


class FishService(Service):

    def initialize_school(self, fitness_function: FitnessFunction):
        school = []
        for i in range(Constants.N_SCHOOL):
            position = self.__generate_initial_position(fitness_function)
            weight = self.__generate_initial_weight()
            fish = Fish(i + 1, position, weight, fitness_function.run(position))
            school.append(fish)
        return school

    @staticmethod
    def __generate_initial_position(fitness_function: FitnessFunction):
        min_value = fitness_function.min_initialization
        max_value = fitness_function.max_initialization
        return np.random.uniform(min_value, max_value, size=(1, Constants.N_DIMENSIONS))

    @staticmethod
    def __generate_initial_weight():
        return Constants.MIN_WEIGHT

