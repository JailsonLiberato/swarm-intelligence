from model.entity import Entity


class Fish(Entity):

    def __init__(self, id, position, weight, fitness):
        self.__id = id
        self.__position = position
        self.__weight = weight
        self.__fitness = fitness

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
