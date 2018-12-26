import matplotlib.pyplot as plt
from DateIterator import DateIterator

class StackPlot(object):
    """Plot the crimes"""

    def __init__(self, crimeList):
        self.crimes = crimeList
        self.dates = []
        self.crimeCount = []
        self.plotData()
        self.line = None
        self.fig = None
        self.ax = None
        self.annot = None

    def plotData(self):
        self.getXDates()
        place = self.crimes[0].location_street_name

        for val in self.dates:
            self.crimeCount.append(self.count(self.crimes, lambda d: d.month == val))       

        self.fig, self.ax = plt.subplots()
        self.line, = plt.plot(self.dates, self.crimeCount, 'bo-', label='All crime count')
        self.annot = plt.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)

        plt.title("All crimes per month " + place)
        plt.xlabel("Date")
        plt.ylabel("Counts")

        self.fig.canvas.mpl_connect("motion_notify_event", self.hover)

        plt.show()

    def update_annot(self, ind):
        x,y = self.line.get_data()
        self.annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        text = self.getMatches(self.annot.xy[0])
        self.annot.set_text(text)
        self.annot.get_bbox_patch().set_alpha(0.4)

    def hover(self, event):
        vis = self.annot.get_visible()
        if event.inaxes == self.ax:
            cont, ind = self.line.contains(event)
            if cont:
                self.update_annot(ind)
                self.annot.set_visible(True)
                self.fig.canvas.draw_idle()
            else:
                if vis:
                    self.annot.set_visible(False)
                    self.fig.canvas.draw_idle()


    def getMatches(self, prop):
        monthData = list(filter(lambda x: x.month == prop, self.crimes))
        text = []
        t = "None"

        if monthData:
            for d in monthData[:-1]:
                text.append(d.getBasicDetails())
                text.append("\n")        
            text.append(monthData[-1].getBasicDetails())
            t = ''.join(text)

        return t

    def count(self, seq, pred):
        return sum(1 for v in seq if pred(v))

    def getXDates(self):
        for dateStr in DateIterator():
            self.dates.append(dateStr)
