from relativedate.dtmath import addMonth, addDay

def lastDay(datetime):
    datetime = addMonth(datetime, 1) # Calcula para o Próximo Mês
    datetime = addDay(datetime.replace(day=1), -1) # Altera a data para o dia 1 e remove 1 dia
    return datetime.day

def lastDate(datetime):    
    return datetime.replace(day=lastDay(datetime), hour=0, minute=0, second=0, microsecond=0)

