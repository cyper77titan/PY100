money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

def func_name(cap, sal, sp):
    remain = cap - sp
    i = 1 # в 7 строчке посчитали расходы за первый месяц (зарплату за него не получили) и это является первым месяцем
    while remain > 0:
        sp = sp * 1.05
        remain = remain - sp + sal
        if remain < 0:    # Если у нас расходы превысили имеющийся бюджет, то выходим из функции и не увеличиваем i
            return i
        i += 1
    return i

month = 0  # количество месяцев, которое можно прожить
month = func_name(money_capital, salary, spend)
# TODO Оформить решение

print(month)



