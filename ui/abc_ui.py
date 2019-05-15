from ui.ui import UI
from business.functions.fitness_function import FitnessFunction
from business.services.abc_service import ArtificialBeeColonyService


class ArtificialBeeColonyUI(UI):

    def __init__(self, fitness_function: FitnessFunction):
        abc_service = ArtificialBeeColonyService(fitness_function)
        super(ArtificialBeeColonyUI, self).__init__(abc_service)
