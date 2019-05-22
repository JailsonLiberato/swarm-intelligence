from model.entity import Entity


class FoodSource(Entity):

    def __init__(self, id, position, fitness):
        self.__id = id
        self.__position = position
        self.__fitness = fitness
        self.__fitness_probability: float = 0.0
        self.__trials: int = 0

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
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness

    @property
    def trials(self):
        return self.__trials

    @trials.setter
    def trials(self, trials):
        self.__trials = trials

    @property
    def fitness_probability(self):
        return self.__fitness_probability

    @fitness_probability.setter
    def fitness_probability(self, fitness_probability):
        self.__fitness_probability = fitness_probability
