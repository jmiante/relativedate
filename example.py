from datetime import datetime
from relativedate import RelativeDate

dt = datetime(year=2023, month=9, day=2)
rd = RelativeDate(dt)
print(rd.getUtilDay(8))
print(rd.getUtilDay(8, [5,19]))

rd.add(year=2, month=-3, day=-300, hour=-500)
print(rd.datetime)
