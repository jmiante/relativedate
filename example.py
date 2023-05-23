from datetime import datetime
from relativedate import RelativeDate

dt = datetime(year=2023, month=5, day=7)

rd = RelativeDate(dt)
print(rd.datetime)

rd.addDay(-27)
print(rd)

rd.addDay(40)
print(rd)
