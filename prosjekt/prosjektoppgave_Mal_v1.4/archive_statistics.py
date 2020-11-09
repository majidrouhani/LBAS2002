import matplotlib.pyplot as plt
#plt.use('TkAgg')  # Fiks for Mac
import numpy as np


def show_histogram_tall(values, min, max, num_bins, ylabel, xlabel):
    bins = np.linspace(min, max, num_bins)
    plt.hist(values, bins)
    plt.show()


def show_histogram1(materialet, counts, ylabel, xlabel):

    plt.bar(materialet, height=materialet)
    plt.xticks(materialet, counts)
    plt.show()

def show_histogram2(materialet, counts, xlabel, ylabel, title):

    #y_pos = np.arange(len(materialet))
    y_pos = range(0,len(materialet))
    plt.bar(y_pos, height=counts)

    plt.title(title)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0,max(counts)+5)

    plt.xticks(y_pos, materialet)
    plt.show()

#Test
show_histogram2(['Tre','Jern','Plast','Glass','Ukategorisert'],[10,5,20,7,50],'Materialet','Antall','Kategori distribusjon')
