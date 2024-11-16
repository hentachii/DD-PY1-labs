salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

pillow = 0
for month in range(months) :
    minus = spend - salary
    pillow += minus
    spend *= (1 + increase)

pillow = round(pillow)

print("Подушка безопасности, чтобы протянуть 10 месяцев без долгов:", pillow)
