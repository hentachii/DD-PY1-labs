money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
pillow = money_capital

while pillow >= 0:
    money = pillow + salary
    if money >= spend:
        pillow -= (spend - salary)
        spend *= (1 + increase)
        month += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month)
