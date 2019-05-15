from ui.ui import UI
from business.functions.fitness_function import FitnessFunction
from business.topologies.topology import Topology
from business.services.pso_service import ParticleSwarmOptimizationService


class ParticleSwarmOptimizationUI(UI):

    def __init__(self, fitness_function: FitnessFunction, topology: Topology):
        pso_service = ParticleSwarmOptimizationService(fitness_function, topology)
        super(ParticleSwarmOptimizationUI, self).__init__(pso_service)
