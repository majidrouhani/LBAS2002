import matplotlib.pyplot as plt
#plt.use('TkAgg')  # Fiks for Mac
import numpy as np


# Lag et histogram hvor gitte verdier telles opp og puttes i bøtter (bins) basert på min, max og antall
def show_histogram(values, min, max, num_bins, ylabel, xlabel):
    bins = np.linspace(min, max, num_bins)
    plt.hist(values, bins)
    plt.show()

# Test-funksjoner
#show_histogram([10,41,72,45,51,52,51,54,56,81,43,42], 0, 100, 10, "Antall", "Alder")
