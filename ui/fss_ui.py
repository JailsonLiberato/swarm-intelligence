from ui.ui import UI
from business.functions.fitness_function import FitnessFunction
from business.services.fss_service import FishSwarmSearchService


class FishSwarmSearchUI(UI):

    def __init__(self, fitness_function: FitnessFunction):
        fss_service = FishSwarmSearchService(fitness_function)
        super(FishSwarmSearchUI, self).__init__(fss_service)
