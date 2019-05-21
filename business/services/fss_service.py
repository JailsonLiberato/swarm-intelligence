from business.services.service import Service
from business.functions.fitness_function import FitnessFunction
from business.services.fish_service import FishService
from util.constants import Constants
import numpy as np
from copy import copy


class FishSwarmSearchService(Service):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fitness_function = fitness_function
        self.__fish_service = FishService()
        self.__school = self.__fish_service.initialize_school(fitness_function)
        self.__fitness_values = []
        self.__gbest = self.__school[0].position
        self.__execute()

    def __execute(self):
        count_fitness: int = 0
        while count_fitness < Constants.N_EVALUATE_FITNESS:
            school_weight_1 = sum(map(lambda x: x.weight, self.__school))
            self.__find_neighbor_position(count_fitness)
            self.__get_delta_position()
            self.__evaluate_fitness()
            count_fitness += Constants.N_PARTICLES
            self.__feed_fish()
            drift = self.__evaluate_drift()
            school_weight_2 = sum(map(lambda x: x.weight, self.__school))
            self.__execute_movement(drift)
            barycenter = self.__calculate_barycenter()
            success = school_weight_2 > school_weight_1
            self.__execute_volitive_movement(barycenter, success, count_fitness)
            self.__update_bound_adjustament()
            best_fitness = self.__get_best_fitness()
            print(count_fitness, " : ", best_fitness)
            self.__fitness_values.append(best_fitness)

    def __update_bound_adjustament(self):
        for fish in self.__school:
            fish.position[fish.position > self.__fitness_function.max_bound] = self.__fitness_function.max_bound
            fish.position[fish.position < self.__fitness_function.min_bound] = self.__fitness_function.min_bound

    def __get_delta_cost_max(self):
        return max(self.__school, key=lambda p: p.delta_fitness)

    def __get_best_fitness(self):
        min_fish = min(self.__school, key=lambda p: p.fitness)
        fitness = self.__fitness_function.run(min_fish.position)
        gbest_fitness = self.__fitness_function.run(self.__gbest)
        if gbest_fitness > fitness:
            self.__gbest = copy(min_fish.position)
            return fitness
        return gbest_fitness

    def __get_delta_position(self):
        for fish in self.__school:
            fish.delta_position = fish.position - fish.neighborhood

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

    def __find_neighbor_position(self, count_fitness):
        for fish in self.__school:
            fish.neighborhood = fish.position + \
                                (self.__generate_step_individual(count_fitness)
                                 * np.random.uniform(-1, 1, size=(1, Constants.N_DIMENSIONS)))

    def __evaluate_fitness(self):
        for fish in self.__school:
            fish.fitness = self.__fitness_function.run(fish.position)
            fish.delta_fitness = self.__fitness_function.run(fish.neighborhood) - self.__fitness_function.run(fish.position)

    def __feed_fish(self):
        for fish in self.__school:
            max_fitness = self.__get_delta_cost_max().delta_fitness
            if max_fitness != 0:
                fish.weight = fish.weight + (fish.fitness / max_fitness)
                if fish.weight < Constants.MIN_WEIGHT:
                    fish.weight = Constants.MIN_WEIGHT

    def __get_min_fitness(self):
        return min(f.fitness for f in self.__school)

    def __evaluate_drift(self):
        a = sum(map(lambda x: x.delta_position * x.delta_fitness, self.__school))
        b = sum(map(lambda x: x.delta_fitness, self.__school))

        if b > 0:
            return a / b
        return np.zeros(self.__school[0].position.shape)

    def __execute_movement(self, drift):
        for fish in self.__school:
            fish.position += drift

    def __calculate_barycenter(self):
        a = sum(map(lambda x: x.position * x.weight, self.__school))
        b = sum(map(lambda x: x.weight, self.__school))
        return a / b

    def __execute_volitive_movement(self, barycenter, success, count_fitness):
        for fish in self.__school:
            a = fish.position - barycenter
            v = self.__generate_step_volitive(count_fitness) * (a / np.linalg.norm(a))
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
