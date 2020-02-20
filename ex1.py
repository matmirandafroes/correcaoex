import datetime
dia_atual = datetime.date.today()

def dias_vida(day_aniv , month_aniv, year_aniv):
    dia_nasc=datetime.date (year=year_aniv, month=month_aniv, day=day_aniv)
    return (dia_atual - dia_nasc)

day_aniv = int(input('Dia do seu aniversário: '))
month_aniv = int(input('Mês do seu aniversário:'))
year_aniv = int(input('ANo do seu aniversário:'))
resultado = dias_vida(day_aniv, month_aniv, year_aniv)
print (resultado)