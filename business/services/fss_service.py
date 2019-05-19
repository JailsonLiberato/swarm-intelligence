from business.services.service import Service


class FishSwarmSearchService(Service):

    def __init__(self):
        self.__fitness_values = []

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values
