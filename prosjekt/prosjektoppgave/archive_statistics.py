import matplotlib as m
import matplotlib.pyplot as plt
#plt.use('TkAgg')  # Fiks for Mac
import numpy as np

# Lag et histogram hvor gitte verdier telles opp og puttes i bøtter (bins) basert på min, max og antall
def show_histogram(materialet, counts, ylabel, xlabel):

    plt.bar(materialet, height=counts)

    plt.xticks(materialet)
    plt.ylim(0,max(counts)*1.1)
    plt.show()

# Test-funksjoner
#show_histogram(['Tre','Glass','Diverse'],[100,41,72],"Materialet", "Antall")
#show_histogram([1,2,3],[100,41,72],"Materialet", "Antall")
