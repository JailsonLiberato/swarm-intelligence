import matplotlib.pyplot as plot


class ChartUtil(object):

    @staticmethod
    def create_curve_line(fitness_values, xlabel, ylabel, title, path):
        plot.plot(fitness_values, label="Fish")
        plot.xlabel(xlabel)
        plot.ylabel(ylabel)
        plot.yscale('log')
        plot.legend()
        plot.title(title)
        plot.savefig(path)
        plot.close()

    @staticmethod
    def create_boxplot(fitness_values, title, path):
        fig = plot.figure(1, figsize=(9, 6))
        ax = fig.add_subplot(111)
        data_to_plot = [fitness_values]
        ax.boxplot(data_to_plot)
        ax.set_xticklabels(['Fish'])
        plot.title(title)
        fig.savefig(path, bbox_inches='tight')
        plot.close()
