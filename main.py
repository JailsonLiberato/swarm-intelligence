from ui.pso_ui import ParticleSwarmOptimizationUI
from ui.abc_ui import ArtificialBeeColonyUI
from ui.fss_ui import FishSwarmSearchUI
from business.functions.sphere_function import SphereFunction
from business.functions.rastringin_function import RastringinFunction
from business.functions.rosenbrock_function import RosenbrockFunction
from business.topologies.local_topology import LocalTopology
from util.constants import Constants
from util.chart_util import ChartUtil


class Main(object):

    def __init__(self):
        self.__sphere_function = SphereFunction()
        self.__rastringin_function = RastringinFunction()
        self.__rosenbrock_function = RosenbrockFunction()
        self.__local_topology = LocalTopology()

    def execute(self):
        self.__create_curve_line()
        self.__create_boxplot()

    def __execute_sphere(self):
        pso_sphere = []#ParticleSwarmOptimizationUI(self.__sphere_function, self.__local_topology).fitness_values
        fss_sphere = FishSwarmSearchUI(self.__sphere_function).fitness_values
        abc_sphere = ArtificialBeeColonyUI(self.__sphere_function).fitness_values
        return pso_sphere, fss_sphere, abc_sphere

    def __execute_rastringin(self):
        pso_rastringin = ParticleSwarmOptimizationUI(self.__rastringin_function).fitness_values
        fss_rastringin = FishSwarmSearchUI(self.__rastringin_function).fitness_values
        abc_rastringin = ArtificialBeeColonyUI(self.__rastringin_function).fitness_values
        return pso_rastringin, fss_rastringin, abc_rastringin

    def __execute_rosenbrock(self):
        pso_rosenbrock = ParticleSwarmOptimizationUI(self.__rosenbrock_function).fitness_values
        fss_rosenbrock = FishSwarmSearchUI(self.__rosenbrock_function).fitness_values
        abc_rosenbrock = ArtificialBeeColonyUI(self.__rosenbrock_function).fitness_values
        return pso_rosenbrock, fss_rosenbrock, abc_rosenbrock

    def __create_curve_line(self):
        ChartUtil.create_curve_line(self.__execute_sphere(), self.__sphere_function.name)
        ChartUtil.create_curve_line(self.__execute_rastringin(), self.__rastringin_function.name)
        ChartUtil.create_curve_line(self.__execute_rosenbrock(), self.__rosenbrock_function.name)

    def __create_boxplot(self):
        pso_fitness_values = []
        fss_fitness_values = []
        abc_fitness_values = []
        for _ in range(Constants.N_ITERATIONS_BOXPLOT):
            pso_sphere, fss_sphere, abc_sphere = self.__execute_sphere()
            pso_fitness_values.append(pso_sphere[len(pso_sphere) - 1])
            fss_fitness_values.append(fss_sphere[len(fss_sphere) - 1])
            abc_fitness_values.append(abc_sphere[len(abc_sphere) - 1])
        ChartUtil.create_boxplot(pso_fitness_values, fss_fitness_values, abc_fitness_values,
                                 self.__sphere_function.name)
        pso_fitness_values = []
        fss_fitness_values = []
        abc_fitness_values = []
        for _ in range(Constants.N_ITERATIONS_BOXPLOT):
            pso_rastringin, fss_rastringin, abc_rastringin = self.__execute_rastringin()
            pso_fitness_values.append(pso_rastringin[len(pso_rastringin) - 1])
            fss_fitness_values.append(fss_rastringin[len(fss_rastringin) - 1])
            abc_fitness_values.append(abc_rastringin[len(abc_rastringin) - 1])
        ChartUtil.create_boxplot(pso_fitness_values, fss_fitness_values, abc_fitness_values,
                                 self.__rastringin_function.name)
        pso_fitness_values = []
        fss_fitness_values = []
        abc_fitness_values = []
        for _ in range(Constants.N_ITERATIONS_BOXPLOT):
            pso_rosenbrock, fss_rosenbrock, abc_rosenbrock = self.__execute_rosenbrock()
            pso_fitness_values.append(pso_rosenbrock[len(pso_rosenbrock) - 1])
            fss_fitness_values.append(fss_rosenbrock[len(fss_rosenbrock) - 1])
            abc_fitness_values.append(abc_rosenbrock[len(abc_rosenbrock) - 1])
        ChartUtil.create_boxplot(pso_fitness_values, fss_fitness_values, abc_fitness_values,
                                 self.__rosenbrock_function.name)


main = Main()
main.execute()
