from business.topologies.topology import Topology
from business.functions.fitness_function import FitnessFunction
import random
from util.constants import Constants
from model.particle import Particle
import numpy as np
from copy import copy


class LocalTopology(Topology):

    def calculate_velocity(self, particles, fitness_function: FitnessFunction):
        self.calculate_lbest(particles, fitness_function)
        inertia = 0.8
        for particle in particles:
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            particle.velocity = (inertia * particle.velocity) + Constants.COEFFICIENT1 * r1 * \
                                (particle.pbest - particle.position) + Constants.COEFFICIENT2 * r2 \
                                * (particle.lbest - particle.position)
        return particles

    @staticmethod
    def calculate_lbest(particles, fitness_function):
        for i in range(len(particles)):
            if i == 0:
                before_particle = particles[len(particles) - 1]
                current_particle = particles[0]
                next_particle = particles[1]
            elif i == len(particles) - 1:
                before_particle = particles[len(particles) - 2]
                current_particle = particles[len(particles) - 1]
                next_particle = particles[0]
            else:
                before_particle = particles[i - 1]
                current_particle = particles[i]
                next_particle = particles[i + 1]

            before_particle.fitness = fitness_function.run(before_particle.pbest)
            current_particle.fitness = fitness_function.run(current_particle.pbest)
            next_particle.fitness = fitness_function.run(next_particle.pbest)

            local_list = [before_particle, current_particle, next_particle]
            local_list.sort(key=lambda x: x.fitness)
            particle: Particle = local_list[0]
            before_particle.lbest = particle.pbest
            current_particle.lbest = particle.pbest
            next_particle.lbest = particle.pbest

    def update_gbest(self, particles, fitness_function: FitnessFunction, gbest):
        for particle in particles:
            if (fitness_function.run(particle.lbest) < fitness_function.run(gbest)) and \
                    self.is_limit_exceeded(fitness_function, particle.lbest):
                gbest = copy(particle.lbest)
        return gbest

    @staticmethod
    def is_limit_exceeded(fitness_function, pbest):
        return np.any(pbest >= fitness_function.min_bound) and np.any(pbest <= fitness_function.max_bound)

