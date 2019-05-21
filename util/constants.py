class Constants(object):

    #GENERAL
    N_DIMENSIONS: int = 30
    N_ITERATIONS_BOXPLOT: int = 30
    N_EVALUATE_FITNESS: int = 500000

    #PSO
    N_PARTICLES: int = 30
    COEFFICIENT1: float = 2.05
    COEFFICIENT2: float = 2.05
    INERTIA_MAX: float = 0.9
    INERTIA_MIN: float = 0.4

    #FSS
    N_SCHOOL: int = 30
    MIN_WEIGHT: float = 1.0
    MAX_INDIVIDUAL: float = 0.1
    MIN_INDIVIDUAL: float = 0.001
    MAX_VOLITIVE: float = 0.01
    MIN_VOLITIVE: float = 0.001

    #ABC
    N_FOOD_SOURCE: int = 30
    EMPLOYED_BEES_PERCENTAGE: float = 0.5
    TRIAL_LIMIT: int = 100
