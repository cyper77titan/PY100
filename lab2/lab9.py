salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


def func_name(sal, sp, m):
    total_money = sp - sal  # сколько денег нужно в первый месяц
    for _ in range(m - 1):
        sp = sp * 1.03
        total_money = total_money + sp - sal
    return total_money



need_money = func_name(salary, spend, months)  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

print(round(need_money))
