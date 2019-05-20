from business.services.service import Service
from business.functions.fitness_function import FitnessFunction
from business.services.fish_service import FishService
from util.constants import Constants


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
            for fish in self.__school:
                self.__find_neighbor_position(fish)
                self.__evaluate_fitness(fish)
                count_fitness += 1
                self.__feed_fish(fish)
            self.__evaluate_drift()
            for fish in self.__school:
                self.__execute_movement(fish)
            self.__calculate_barycenter()
            for fish in self.__school:
                self.__execute_volitive_movement(fish)
            self.__update_individual_evolution()

    def __find_neighbor_position(self, fish):
        pass

    def __evaluate_fitness(self, fish):
        fish.fitness = self.__fitness_function.run(fish)

    def __feed_fish(self, fish):
        pass

    def __evaluate_drift(self):
        pass

    def __execute_movement(self, fish):
        pass

    def __calculate_barycenter(self):
        pass

    def __execute_volitive_movement(self, fish):
        pass

    def __update_individual_evolution(self):
        pass

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values
