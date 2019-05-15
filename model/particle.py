import numpy as np
from util.constants import Constants
from copy import copy
from model.entity import Entity


class Particle(Entity):

    def __init__(self, id, position, fitness):
        self.__fitness = fitness
        self.__id = id
        self.__position = position
        self.__pbest = copy(position)
        self.__velocity = np.zeros(Constants.N_DIMENSIONS)
        self.__lbest = []

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
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    @property
    def pbest(self):
        return self.__pbest

    @pbest.setter
    def pbest(self, pbest):
        self.__pbest = pbest

    @property
    def lbest(self):
        return self.__lbest

    @lbest.setter
    def lbest(self, lbest):
        self.__lbest = lbest

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness
