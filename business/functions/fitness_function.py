class FitnessFunction(object):

    def __init__(self, name, bounds, inits):
        self.__name = name
        self.__min_bound = bounds[0]
        self.__max_bound = bounds[1]
        self.__min_initialization = inits[0]
        self.__max_initialization = inits[1]

    @property
    def name(self):
        return self.__name

    @property
    def min_bound(self):
        return self.__min_bound

    @property
    def max_bound(self):
        return self.__max_bound

    @property
    def min_initialization(self):
        return self.__min_initialization

    @property
    def max_initialization(self):
        return self.__max_initialization
