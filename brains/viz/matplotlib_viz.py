# visualization functions

# BUG 15 fix: This might just be a pycharm problem
import matplotlib
matplotlib.use('TkAgg') # probably a better way to set this, but this works for now

from matplotlib import pyplot as plt

def histogram(data,xlabel=None,ylabel="counts",title=None):
    """
    Display a histogram of the data

    :param data: e.g. a single column of dataframe (does it have to be numerical? maybe works for multiple columns)
    :param xlabel: label for x-axis
    :param ylabel:
    :param title:
    :return: display the plot
    """
    # TODO add feature selection

    # generate histogram
    plt.hist(data)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    if title is not None:
        plt.title(title)

    #TODO determine how to actually display something -- maybe we return the plt instead
    plt.show()
    # TODO save as a png or return the fig by returning plt somehow?
