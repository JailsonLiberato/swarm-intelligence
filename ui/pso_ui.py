from ui.ui import UI
from business.functions.fitness_function import FitnessFunction
from business.topologies.topology import Topology
from business.services.pso_service import ParticleSwarmOptimizationService


class ParticleSwarmOptimizationUI(UI):

    def __init__(self, fitness_function: FitnessFunction, topology: Topology):
        pso_service = ParticleSwarmOptimizationService(fitness_function, topology)
        self.__fitness_values = pso_service.fitness_values

    @property
    def fitness_values(self):
        return self.__fitness_values

