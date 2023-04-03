src = not False and True or False and not True

# src = True and True or False and False # меняем на противоположные значения True/False, чтобы избавиться от not
# src = True or False # избавляемся от and
# src = True # избавляемся от or
# TODO расписать упрощение выражения

result = True  # TODO подставить результат выражения

print(src == result)
