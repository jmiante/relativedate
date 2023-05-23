from datetime import datetime as dt
from relativedate import dtmath, dtget


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

    ### DATE MATH ###
    def addDay(self, relative_day):
        self.datetime = dtmath.addDay(self.datetime, relative_day)

    def addMonth(self, relative_month):
        self.datetime = dtmath.addMonth(self.datetime, relative_month)

    def addYear(self, relative_year):
        self.datetime = dtmath.addYear(self.datetime, relative_year)

    def add(self, year=0, month=0, day=0, hour=0, minute=0, second=0):
        self.datetime = dtmath.add(datetime=self.datetime,year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    def dateDiff(self, datetime):
        return dtmath.dateDiff(self.datetime, datetime)
    
    ### DATE GET ###
    def lastDay(self):
        return dtget.lastDay(self.datetime)
    
    def lastDate(self):
        return dtget.lastDate(self.datetime)

