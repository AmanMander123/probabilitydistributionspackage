import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Gaussian(Distribution):
    """
    Gaussian distribution class for calculating and visualizing a Gaussian
    distribution

    Attributes:
            mean (float):  representing the mean value of the distribution
            stdev (float):  representing the standard deviation of the
                            distribution
            data_list (list of floats): data points extracted from the data
                                        file
    """

    def __init__(self, mu=0, sigma=1):
        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):
        """
        Function to calculate mean of the data set

        :return: float representing the mean of the data set
        """
        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Function to calculate standard deviation of the data set

        :param sample: bool representing whether the data set represents
        a sample (True) or population (False)
        :return: float representing standard deviation of the data set
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.calculate_mean()
        sigma = 0
        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma / n)
        self.stdev = sigma
        return self.stdev

    def plot_histogram(self):
        """
        Function to output a histogram of the instance variable data using
        the matplotlib library

        :return: None
        """

        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('Data')
        plt.ylabel('Count')

    def pdf(self, x):
        """
        Probability density function calculator for the Gaussian distribution

        :param x: float representing the point for calculating the
        probability density function
        :return: float representing the probability density output
        """

        return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.mean) / self.stdev) ** 2)

    def plot_histogram_pdf(self, n_spaces=50):
        """
        Function to plot the normalized histogram of the data and a plot of the
		probability density function along the same range
        :param n_spaces: integer representing the number of data points
        :return: x, y values for the pdf plot
        """

        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # calculate the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):
        """
        Function to add together two Gaussian distributions
        :param other: Gaussian instance to add
        :return: Gaussian distribution
        """

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        return result

    def __repr__(self):
        """
        Function to output the characteristics of the Gaussian instance
        :return: string representing the characteristics of the Gassian
        distribution
        """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

