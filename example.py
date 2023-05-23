from datetime import datetime
from relativedate import RelativeDate

dt = datetime(year=2022, month=9, day=2)
dt2 = datetime(year=2023, month=5, day=20)

rd = RelativeDate(dt)
print(rd.datetime)
print(dt2)

date_diff = rd.dateDiff(dt2)
print(date_diff)
