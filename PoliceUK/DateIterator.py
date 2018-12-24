from datetime import datetime

class DateIterator(object):
    """description of class"""

    def __init__(self):
        self.year_min = 2015
        self.currentYear = 2015
        self.currentMonth = 12


    def __iter__(self):
        return self

    def __next__(self):
        dateObj = datetime.now()
        if self.currentYear >= dateObj.year and self.currentMonth >= dateObj.month:
            raise StopIteration
        else:
            dateStr = "{}-{}".format(str(self.currentYear), str(self.currentMonth).zfill(2))

            self.currentMonth +=1
            if self.currentMonth > 12:
                self.currentMonth = 1
                self.currentYear +=1

            return dateStr



