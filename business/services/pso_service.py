from business.services.service import Service
from business.functions.fitness_function import FitnessFunction
from business.topologies.topology import Topology


class ParticleSwarmOptimizationService(Service):

    def __init__(self, fitness_function: FitnessFunction, topology: Topology):
        self.__fitness_function = fitness_function
        self.__topology = topology
        self.__execute()

    def __execute(self):
        pass
