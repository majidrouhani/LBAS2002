import matplotlib as m
import matplotlib.pyplot as plt
#plt.use('TkAgg')  # Fiks for Mac
import numpy as np


# Lag en "bar-chart" med gitte verdier på x-aksen, og antall for hver av dem
def show_bar_chart(counts, labels, ylabel, xlabel):
    x = np.arange(len(counts))
    m.bar(x, height=counts)
    m.xticks(x, labels)
    m.ylabel(ylabel)
    m.xlabel(xlabel)
    m.show()

# Lag et histogram hvor gitte verdier telles opp og puttes i bøtter (bins) basert på min, max og antall
def show_histogram(values, min, max, num_bins, ylabel, xlabel):
    bins = np.linspace(min, max, num_bins)
    plt.hist(values, bins)
    plt.show()

# Test-funksjoner
#show_bar_chart([2, 16, 3, 1, 4.5], ["a", "b", "c", "d", "e"], "Antall", "Kategori")
show_histogram([10,41,72,45,51,52,51,54,56,81,43,42], 0, 100, 10, "Antall", "Alder")
