from datetime import datetime as dt


class RelativeDate:
    def __init__(self, datetime=None):
        if datetime is None:
            self.datetime = dt.now()
        else:
            self.datetime = datetime

        self.year = self.datetime.year
        self.month = self.datetime.month
        self.day = self.datetime.day
        self.hour = self.datetime.hour
        self.minute = self.datetime.minute
        self.second = self.datetime.second
    
    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d')

    def get_relative_month(self, relative_month):
        mes = self.month + relative_month
        ano = self.year
            
        # Tratado Ano
        if abs(relative_month) > 12:
            ano_delta = int(relative_month / 12)
            ano += ano_delta
            mes += (abs(ano_delta) * 12) 
        
        # Tratamento do Mês
        if mes < 1: 
            mes += 12
            ano -= 1
        elif mes > 12: 
            mes -= 12
            ano += 1
        return self.datetime.replace(year=ano, month=mes)

    