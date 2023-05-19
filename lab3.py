import random
def get_unique_list_numbers() -> list[int]:
    list_of_numbers = []
    for _ in range(15):
        number: int = random.randint(-10, 10)
        while list_of_numbers.count(number) > 0:
            number: int = random.randint(-10, 10)
        list_of_numbers.append(number)
        set(list_of_numbers)
    return list_of_numbers
    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
