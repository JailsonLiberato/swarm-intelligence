from model.entity import Entity


class FoodSource(Entity):

    def __init__(self, position):
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position - position
