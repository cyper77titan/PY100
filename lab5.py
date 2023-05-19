import random
import string



def get_random_password() -> str:
    list_ = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits)
    password = random.sample(list_, 8)
    return ''.join(password) # Преобразование из списка в строку для красоты
    ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())
