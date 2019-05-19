from ui.ui import UI
from business.functions.fitness_function import FitnessFunction
from business.services.abc_service import ArtificialBeeColonyService


class ArtificialBeeColonyUI(UI):

    def __init__(self, fitness_function: FitnessFunction):
        abc_service = ArtificialBeeColonyService(fitness_function)
        self.__fitness_values = abc_service.fitness_values

    @property
    def fitness_values(self):
        return self.__fitness_values
