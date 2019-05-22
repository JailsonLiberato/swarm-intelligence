from model.particle import Particle
from util.constants import Constants
import numpy as np
from business.functions.fitness_function import FitnessFunction
from business.services.service import Service


class ParticleService(Service):

    def initialize_particles(self, fitness_function: FitnessFunction):
        particles = []
        for i in range(Constants.N_PARTICLES):
            position = self.generate_initial_position(fitness_function)
            particle = Particle(i + 1, position, fitness_function.run(position))
            particles.append(particle)
        return particles

    @staticmethod
    def generate_initial_position(fitness_function: FitnessFunction):
        min_value = fitness_function.min_initialization
        max_value = fitness_function.max_initialization
        return np.random.uniform(min_value, max_value, size=(1, Constants.N_DIMENSIONS))[0]
