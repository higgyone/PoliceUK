from datetime import datetime

class DateIterator(object):
    """Iterate through the available dates"""

    def __init__(self):
        self.currentYear = 2015
        self.currentMonth = 12


    def __iter__(self):
        return self

    def __next__(self):
        """Return the next date in year-month YYYY-MM format up to the current month"""
        dateObj = datetime.now()

        if self.currentYear >= dateObj.year and self.currentMonth >= dateObj.month:
            raise StopIteration
        else:
            """date string should be e.g.'2018-08' for August 2018"""
            dateStr = "{}-{}".format(str(self.currentYear), str(self.currentMonth).zfill(2))

            self.currentMonth +=1
            if self.currentMonth > 12:
                self.currentMonth = 1
                self.currentYear +=1

            return dateStr



