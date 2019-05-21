from business.services.service import Service
from business.functions.fitness_function import FitnessFunction
from business.topologies.topology import Topology
from util.constants import Constants
from business.services.particle_service import ParticleService
import numpy as np
from copy import copy


class ParticleSwarmOptimizationService(Service):

    def __init__(self, fitness_function: FitnessFunction, topology: Topology):
        self.__fitness_function = fitness_function
        self.__topology = topology
        self.__fitness_values = []
        self.__particle_service = ParticleService()
        self.__particles = self.__particle_service.initialize_particles(self.__fitness_function)
        self.__gbest = self.__particles[0].pbest
        self.__execute()

    def __execute(self):
        count_iterations: int = 0
        while count_iterations < Constants.N_EVALUATE_FITNESS:
            self.__calculate_fitness()
            count_iterations += Constants.N_PARTICLES
            self.__update_gbest()
            inertia = self.__generate_inertia(count_iterations)
            self.__particles = self.__topology.calculate_velocity(self.__particles, inertia, self.__fitness_function)
            self.update_position()
            self.update_bound_adjustament()
            best_value = self.__fitness_function.run(self.__gbest)
            print(count_iterations, " : ", best_value)
            self.__fitness_values.append(best_value)

    def __calculate_fitness(self):
        for particle in self.__particles:
            if self.__fitness_function.run(particle.position) < self.__fitness_function.run(particle.pbest):
                particle.pbest = copy(particle.position)
                particle.fitness = self.__fitness_function.run(particle.position)

    def __update_gbest(self):
        for particle in self.__particles:
            if self.__fitness_function.run(particle.pbest) < self.__fitness_function.run(self.__gbest):
                self.__gbest = particle.pbest

    @staticmethod
    def __generate_inertia(count_iterations):
        return Constants.INERTIA_MAX - count_iterations * (Constants.INERTIA_MAX - Constants.INERTIA_MIN) / \
                   Constants.N_EVALUATE_FITNESS

    def update_position(self):
        for particle in self.__particles:
            particle.position += particle.velocity

    def update_bound_adjustament(self):
        for particle in self.__particles:
            particle.position[particle.position > self.__fitness_function.max_bound] = self.__fitness_function.max_bound
            particle.position[particle.position < self.__fitness_function.min_bound] = self.__fitness_function.min_bound

    @property
    def fitness_values(self):
        return self.__fitness_values

    @fitness_values.setter
    def fitness_values(self, fitness_values):
        self.__fitness_values = fitness_values

