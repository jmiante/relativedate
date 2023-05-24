from datetime import datetime
from relativedate.dtmath import addMonth, addDay

def lastDay(dt):
    dt = addMonth(dt, 1) # Calcula para o Próximo Mês
    dt = addDay(dt.replace(day=1), -1) # Altera a data para o dia 1 e remove 1 dia
    return dt.day

def lastDate(dt):    
    return dt.replace(day=lastDay(dt), hour=0, minute=0, second=0, microsecond=0)

def getUtilDay(dt, util_day, disregard=[]):
    util_day = util_day
    util = 0
    for day in [datetime(dt.year, dt.month, d) for d in range(1, lastDay(dt)+1)]:
        if day.weekday() not in (5,6) and day.day not in disregard:
            util += 1
            if util == util_day:
                return day
            
def utilDays(dt, disregard=[]):
    util = 0
    for day in [datetime(dt.year, dt.month, d) for d in range(1, lastDay(dt)+1)]:
        if day.weekday() not in (5,6) and day.day not in disregard:
            util += 1
    return util
