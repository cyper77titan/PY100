# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
def new_number(number):
    final_dictionary = {'bin': bin(number), 'dec' : number, 'hex': hex(number), 'oct': oct(number)}
    return final_dictionary
new_list = [new_number(iterator) for iterator in range(0, 16, 1)]
pprint(new_list)