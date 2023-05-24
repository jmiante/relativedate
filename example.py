from datetime import datetime
from relativedate import RelativeDate

dt = datetime(year=2023, month=9, day=2)
rd = RelativeDate(dt)
print(rd.getUtilDay(8))
print(rd.getUtilDay(8, [5,19]))