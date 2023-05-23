from datetime import datetime as dt
from relativedate import dtmath


class RelativeDate:
    def __init__(self, datetime=None):
        if datetime is None:
            self.datetime = dt.now()
        else:
            self.datetime = datetime

        self.year = self.datetime.year
        self.month = self.datetime.month
        self.day = self.datetime.day
        self.hour = self.datetime.hour
        self.minute = self.datetime.minute
        self.second = self.datetime.second
    
    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d')

    def addDay(self, relative_day):
        self.datetime = dtmath.addDay(self.datetime, relative_day)

    def addMonth(self, relative_month):
        self.datetime = dtmath.addMonth(self.datetime, relative_month)

    def addYear(self, relative_year):
        self.datetime = dtmath.addYear(self.datetime, relative_year)
