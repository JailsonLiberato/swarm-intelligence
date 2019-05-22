import matplotlib.pyplot as plot


class ChartUtil(object):

    @staticmethod
    def create_curve_line(fitness_values, title):
        pso_fitness_values, fss_fitness_values, abc_fitness_values = fitness_values
        plot.plot(pso_fitness_values, label="PSO")
        plot.plot(fss_fitness_values, label="FSS")
        plot.plot(abc_fitness_values, label="ABC")
        plot.xlabel("Number of iterations")
        plot.ylabel("Fitness")
        plot.yscale('log')
        plot.legend()
        plot.title("Curve Line: " + title)
        name_file = title.lower()
        plot.savefig('file//curve_line_' + name_file + '.png')
        plot.close()

    @staticmethod
    def create_boxplot(pso_fitness_values, fss_fitness_values, abc_fitness_values, title):
        fig = plot.figure(1, figsize=(9, 6))
        ax = fig.add_subplot(111)
        data_to_plot = [pso_fitness_values, fss_fitness_values, abc_fitness_values]
        ax.boxplot(data_to_plot)
        ax.set_xticklabels(['PSO', 'FSS', 'ABC'])
        plot.title("Boxplot: " + title)
        name_file = title.lower()
        fig.savefig('..//file//boxplot_' + name_file + '.png', bbox_inches='tight')
        plot.close()


#chartUtil = ChartUtil()
#x = [1.2, 3.2], [5.2, 4.2], [4.2, 2.2]
#chartUtil.create_curve_line(x, "Sphere")
