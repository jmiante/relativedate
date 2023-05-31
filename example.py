from datetime import datetime
from relativedate import RelativeDate

dt = datetime(year=2023, month=9, day=2)
dt = datetime.now()
print(dt)
rd = RelativeDate(dt)
rd.addMonth(1)
#print(rd.datetime)
#print(rd.getUtilDay(30, last_day=True))
