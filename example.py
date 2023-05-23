from datetime import datetime
from relativedate import RelativeDate

dt = datetime(year=2023, month=5, day=7)

rd = RelativeDate(dt)
print(rd)

rd.addMonth(-29)
print(rd)
