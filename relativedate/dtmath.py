from datetime import timedelta

def addYear(dt, relative_year):
    try:
        year = dt.year + int(relative_year)
    except:
         raise Exception('O atributo relative_year deve ser do tipo INT')
    return dt.replace(year=year)

def addMonth(dt, relative_month):
        """
        """
        month = dt.month + relative_month
        year = dt.year
            
        # Tratado Ano
        if abs(relative_month) > 12:
            year_delta = int(relative_month / 12)
            year += year_delta
            month += (abs(year_delta) * 12) 
        
        # Tratamento do Mês
        if month < 1: 
            month += 12
            year -= 1
        elif month > 12: 
            month -= 12
            year += 1
        return dt.replace(year=year, month=month)

def addDay(dt, relative_day):
     return dt + timedelta(days=relative_day)


def add(dt, year=0, month=0, day=0, hour=0, minute=0, second=0):
    dt = dt
    if month != 0:
        dt = addMonth(dt, month)
    if year != 0:
        dt = addYear(dt, year)
    return dt + timedelta(days=day, hours=hour, minutes=minute, seconds=second)

def dateDiff(first_dt, second_dt):
     return second_dt - first_dt
    
