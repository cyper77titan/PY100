list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
unique_data = set(list_)

print(sum(unique_data))
print(len(unique_data))
print(round(sum(unique_data) / len(unique_data), 5))
