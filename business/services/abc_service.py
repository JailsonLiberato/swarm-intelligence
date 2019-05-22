from business.services.service import Service
from business.functions.fitness_function import FitnessFunction
from business.services.food_source_service import FoodSourceService
from util.constants import Constants
import random as rand
import numpy as np
from copy import copy


class ArtificialBeeColonyService(Service):

    def __init__(self, fitness_function: FitnessFunction):
        self.__fitness_function = fitness_function
        self.__fitness_values = []
        self.__employed_bees = round(Constants.N_FOOD_SOURCE * Constants.EMPLOYED_BEES_PERCENTAGE)
        self.__onlooker_bees = Constants.N_FOOD_SOURCE - self.__employed_bees
        self.__food_source_service = FoodSourceService()
        self.__food_sources = self.__food_source_service.initialize_food_source(self.__fitness_function)
        self.__gbest = copy(self.__food_sources[0].position)
        self.__evaluate_fitness()
        self.__execute()

    def __execute(self):
        count_fitness: int = 0
        while count_fitness < Constants.N_EVALUATE_FITNESS:
            count_fitness += Constants.N_FOOD_SOURCE
            self.__employed_bees_stage()
            self.__onlooker_bees_stage()
            self.__scout_bees_stage()
            value = self.__get_best_source()
            self.__fitness_values.append(value)
            print(count_fitness, " : ", value)
        return self.__fitness_values

    def __get_best_source(self):
        min_food_source = min(self.__food_sources, key=lambda p: p.fitness)
        fitness = self.__fitness_function.run(min_food_source.position)
        gbest_fitness = self.__fitness_function.run(self.__gbest)
        if gbest_fitness > fitness:
            self.__gbest = copy(min_food_source.position)
            return fitness
        return gbest_fitness

    def __scout_bees_stage(self):
        for i in range(self.__employed_bees):
            food_source = self.__food_sources[i]
            if food_source.trials > Constants.TRIAL_LIMIT:
                food_source = self.__food_source_service.create_foodsource(self.__fitness_function, food_source.id)

    @staticmethod
    def selection(solutions, weights):
        return rand.choices(solutions, weights)[0]

    def __probability(self, solution_fitness):
        fitness_sum = sum([fs.fitness_probability for fs in self.__food_sources])
        probability = solution_fitness.fitness_probability / fitness_sum
        return probability

    def __onlooker_bees_stage(self):
        for i in range(self.__onlooker_bees):
            probabilities = [self.__probability(fs) for fs in self.__food_sources]
            selected_index = self.selection(range(len(self.__food_sources)), probabilities)
            selected_source = self.__food_sources[selected_index]
            new_position = self.__generate_position(selected_index)
            best_position = self.__best_position(selected_source.position, new_position)

            self.__set_position(selected_source, best_position)

    def __employed_bees_stage(self):
        for i in range(self.__employed_bees):
            food_source = self.__food_sources[i]
            new_position = self.__generate_position(i)
            best_position = self.__best_position(food_source.position, new_position)
            self.__set_position(food_source, best_position)

    def __set_position(self, food_source, new_position):
        if np.array_equal(new_position, food_source.position):
            food_source.trials += 1
        else:
            food_source.position = copy(new_position)
            food_source.trials = 0

    def __best_position(self, current_position, new_position):
        if self.__fitness_function.run(new_position) < self.__fitness_function.run(current_position):
            return new_position
        else:
            return current_position

    def __generate_position(self, current_solution_index):
        position = self.__food_sources[current_solution_index].position
        k_source_index = self.__random_solution_excluding([current_solution_index])
        k_position = self.__food_sources[k_source_index].position
       # d = rand.randint(0, 1) #d = rand.randint(0, len(self.fn_lb) - 1) #Verificar as dimensões
        r = rand.uniform(-1, 1)
        #new_position = np.copy(position)
        new_position = position + r * (position - k_position)
        return np.around(new_position, decimals=4)

    def __random_solution_excluding(self, food_source):
        available_indexes = set(range(self.__employed_bees))
        exclude_set = set(food_source)
        diff = available_indexes - exclude_set
        selected = rand.choice(list(diff))

        return selected

    def __evaluate_fitness(self):
        for food_source in self.__food_sources:
            result = self.__fitness_function.run(food_source.position)
            food_source.fitness = result
            if result >= 0:
                food_source.fitness_probability = 1 / (1 + result)
            else:
                food_source.fitness_probability = abs(result)

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values

