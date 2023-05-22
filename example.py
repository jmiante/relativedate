from datetime import datetime
from relativedate import RelativeDate

dt = datetime(year=2023, month=5, day=7)

print(dt)

rd = RelativeDate(dt)
print(rd.get_relative_month(-29))