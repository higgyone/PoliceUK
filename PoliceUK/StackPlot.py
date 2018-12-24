import numpy as np
import matplotlib.pyplot as plt
from DateIterator import DateIterator

class StackPlot(object):
    """Plot the crimes"""

    def __init__(self, crimeList):
        self.crimes = crimeList
        self.dates = []
        self.crimeCount = []
        self.plotData()

    def plotData(self):
        self.getXDates()

        for val in self.dates:
            self.crimeCount.append(self.count(self.crimes, lambda d: d.month == val))

        plt.stackplot(self.dates, [self.crimeCount], colors=['#377EB8'])
        plt.show()


    def count(self, seq, pred):
        return sum(1 for v in seq if pred(v))

    def getXDates(self):
        for dateStr in DateIterator():
            self.dates.append(dateStr)
