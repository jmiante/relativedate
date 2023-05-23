from datetime import timedelta

def addYear(datetime, relative_year):
    try:
        year = datetime.year + int(relative_year)
    except:
         raise Exception('O atributo relative_year deve ser do tipo INT')
    return datetime.replace(year=year)

def addMonth(datetime, relative_month):
        """
        """
        month = datetime.month + relative_month
        year = datetime.year
            
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
        return datetime.replace(year=year, month=month)

def addDay(datetime, relative_day):
     return datetime + timedelta(days=relative_day)

