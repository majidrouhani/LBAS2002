import matplotlib
matplotlib.use('TkAgg')  # Fiks for Mac
#import matplotlib.pyplot as plt
import numpy as np


# Lag en "bar-chart" med gitte verdier på x-aksen, og antall for hver av dem
def show_bar_chart(counts, labels, ylabel, xlabel):
    x = np.arange(len(counts))
    matplotlib.bar(x, height=counts)
    matplotlib.xticks(x, labels)
    matplotlib.ylabel(ylabel)
    matplotlib.xlabel(xlabel)
    matplotlib.show()

# Lag et histogram hvor gitte verdier telles opp og puttes i bøtter (bins) basert på min, max og antall
def show_histogram(values, min, max, num_bins, ylabel, xlabel):
    bins = np.linspace(min, max, num_bins)
    matplotlib.hist(values, bins)
    matplotlib.ylabel(ylabel)
    matplotlib.xlabel(xlabel)
    matplotlib.show()

# Test-funksjoner
#show_bar_chart([2, 16, 3, 1, 4.5], ["a", "b", "c", "d", "e"], "Antall", "Kategori")
#show_histogram([10,41,72,45,51,52,51,54,56,81,43,42], 0, 100, 10, "Antall", "Alder")
