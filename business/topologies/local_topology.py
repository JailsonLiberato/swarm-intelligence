from business.topologies.topology import Topology
from business.functions.fitness_function import FitnessFunction
import random
from util.constants import Constants


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

    @staticmethod
    def update_gbest(particles, fitness_function: FitnessFunction, gbest):
        for particle in particles:
            if fitness_function.run(particle.lbest) < fitness_function.run(gbest):
                gbest = particle.lbest
        return gbest
