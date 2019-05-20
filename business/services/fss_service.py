from business.services.service import Service
from business.functions.fitness_function import FitnessFunction
from business.services.fish_service import FishService
from util.constants import Constants
import numpy as np


class FishSwarmSearchService(Service):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fitness_function = fitness_function
        self.__fish_service = FishService()
        self.__school = self.__fish_service.initialize_school(fitness_function)
        self.__fitness_values = []
        self.__execute()

    def __execute(self):
        count_fitness: int = 0
        while count_fitness < Constants.N_EVALUATE_FITNESS:
            school_weight_1 = sum(map(lambda x: x.weight, self.__school))
            for fish in self.__school:
                self.__find_neighbor_position(fish, count_fitness)
                self.__evaluate_fitness(fish)
                count_fitness += 1
                self.__feed_fish(fish)
            drift = self.__evaluate_drift()
            school_weight_2 = sum(map(lambda x: x.weight, self.__school))
            for fish in self.__school:
                self.__execute_movement(fish, drift)
            barycenter = self.__calculate_barycenter()
            success = school_weight_2 > school_weight_1
            for fish in self.__school:
                self.__execute_volitive_movement(fish, barycenter, success, count_fitness)
                self.__update_step_individual(fish, count_fitness)
            self.__fitness_values.append(self.__get_best_fitness().fitness)

    def __get_best_fitness(self):
        return min(self.__school, key=lambda p: p.fitness)

    def __update_step_individual(self, fish, count_fitness):
        fish.position = fish.position + \
                            (self.__generate_step_individual(count_fitness)
                             * np.random.uniform(-1, 1, size=(1, Constants.N_DIMENSIONS)))

    @staticmethod
    def __generate_step_individual(count_fitness):
        return Constants.MAX_INDIVIDUAL - (((Constants.MAX_INDIVIDUAL - Constants.MIN_INDIVIDUAL)
                                            * count_fitness) / Constants.N_EVALUATE_FITNESS)

    @staticmethod
    def __generate_step_volitive(count_fitness):
        return Constants.MAX_VOLITIVE - (((Constants.MAX_VOLITIVE - Constants.MIN_VOLITIVE)
                                            * count_fitness) / Constants.N_EVALUATE_FITNESS)

    def __find_neighbor_position(self, fish, count_fitness):
        fish.neighborhood = fish.position + \
                            (self.__generate_step_individual(count_fitness)
                             * np.random.uniform(-1, 1, size=(1, Constants.N_DIMENSIONS)))

    def __evaluate_fitness(self, fish):
        fish.fitness = self.__fitness_function.run(fish.neighborhood) - self.__fitness_function.run(fish.position)

    def __feed_fish(self, fish):
        max_fitness = max(f.fitness for f in self.__school)
        fish.weight = fish.weight + (fish.fitness / max_fitness)

    def __get_min_fitness(self):
        return min(f.fitness for f in self.__school)

    def __evaluate_drift(self):
        a = sum(map(lambda x: x.position * x.fitness, self.__school))
        b = sum(map(lambda x: x.fitness, self.__school))

        if b > 0:
            return a / b
        return np.zeros(self.__school[0].position.shape)

    @staticmethod
    def __execute_movement(fish, drift):
        fish.position += drift

    def __calculate_barycenter(self):
        a = sum(map(lambda x: x.position * x.weight, self.__school))
        b = sum(map(lambda x: x.weight, self.__school))
        return a / b

    def __execute_volitive_movement(self, fish, barycenter, success, count_fitness):
        a = fish.position - barycenter
        random_step = np.random.uniform(0, 1, fish.position.shape)
        v = self.__generate_step_volitive(count_fitness) * (a / np.linalg.norm(a)) * random_step
        if success:
            fish.position -= v
        else:
            fish.position += v

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values
