import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
        place = self.crimes[0].location_street_name

        for val in self.dates:
            self.crimeCount.append(self.count(self.crimes, lambda d: d.month == val))
        
        plt.plot(self.dates, self.crimeCount, 'bo-', label='All crime count')
        plt.legend()
        #plt.stackplot(self.dates, [self.crimeCount], colors=['#377EB8'])

       # plt.legend([mpatches.Patch(color='#377EB8')], ['All Crime Count'])
        plt.title("All crimes per month " + place)
        plt.xlabel("Date")
        plt.ylabel("Counts")

        plt.show()


    def count(self, seq, pred):
        return sum(1 for v in seq if pred(v))

    def getXDates(self):
        for dateStr in DateIterator():
            self.dates.append(dateStr)
