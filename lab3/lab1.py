def get_count_char(str_):
    dictionary = {}
    for character in str_:
        if not character.isalpha():
            continue
        if dictionary.get(character):
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary

def percentage (inp): # функция для оперделения % каждой буквы в строке
    total = sum(inp.values())
    for key, value in inp.items():
        inp[key] = round(value / total * 100, 2) # округляем % до двух знаков после запятой
    return inp


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str.lower()))
a = get_count_char(main_str.lower())
print(percentage(a))
