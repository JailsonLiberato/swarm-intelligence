from model.entity import Entity


class Fish(Entity):

    def __init__(self, id, position, weight, fitness):
        self.__id = id
        self.__position = position
        self.__weight = weight
        self.__fitness = fitness
        self.__delta_fitness: float = 0.0
        self.__delta_position: float = 0.0
        self.__neighborhood = 0.0

    @property
    def id(self):
        return self.__id

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness

    @property
    def delta_fitness(self):
        return self.__delta_fitness

    @delta_fitness.setter
    def delta_fitness(self, delta_fitness):
        self.__delta_fitness = delta_fitness

    @property
    def delta_position(self):
        return self.__delta_position

    @delta_position.setter
    def delta_position(self, delta_position):
        self.__delta_position = delta_position

    @property
    def neighborhood(self):
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood

