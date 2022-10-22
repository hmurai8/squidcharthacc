# visualization functions

from matplotlib import pyplot as plt
plt.interactive(False) # @penguinyaro needed this to make my plots show in his pycharm
# TODO probably remove above later

def histogram(data,xlabel,ylabel,title):
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

    #TODO determine how to actually display something
    plt.show()