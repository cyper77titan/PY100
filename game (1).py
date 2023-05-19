from typing import Union, List, Tuple, Optional
import random

EMPTY_CELL = " "


def init_field(size: int, empty_cell: str = EMPTY_CELL) -> List[List[str]]:
    """
    Создаёт и возвращает пустое поля для игры
    :param size: Размер поля
    :param empty_cell: Чем заполняем пустую ячейку поля
    :return: Пустое поле [[" "],...]
    """

    return [[empty_cell] * size for _ in range(size)]

def start_field_for_computer(size: int) -> List[List[int]]:
    """
    Создаёт первоначальный список с индексами пустых ячеек. именно так компьютер понимает куда можно ходить
    :param size: Размер поля
    :return: список с номерами пустых ячеек
    """
    list_of_index = []
    for row in range(size):
        for column in range(size):
            list_of_index.append(row * 10 + column)
    return list_of_index


def draw_field(field: List[List[str]]) -> None:
    """
    Рисует поле

    | | | |
    | | | |
    | | | |

    :param field: массив с ходами игроков
    :return: ничего не возвращает
    """
    for row in field:
        for cell in row:
            print(f"|{cell}", end="")
        print("|")


def get_int_val(text: str, border_min: Optional[int] = None, border_max: Optional[int] = None) -> int:
    """
    Проверяет и возвращает целое число
    :param text: Сообщение для пользователя
    :param border_min: нижняя граница диапазона выбора
    :param border_max: верхняя граница диапазона выбора
    :return: Возвращает выбранное пользователем число
    """
    while True:
        val = input(text)
        try:
            val = int(val)
        except ValueError:
            print("Должно быть целым")
            continue
            # return get_int_val(text, border_min, border_max)
        if border_min is not None and border_max is not None:
            if not (border_min <= val <= border_max):
                print(f"Значение должно лежать в диапазоне ({border_min}, {border_max})")
                continue
        return val


def get_char_val(text: str, req_char: list) -> str:
    """
    Проверяет и возвращает строку
    :param text: Сообщение для пользователя
    :param req_char: Список допустимых значений
    :return: Введённое пользователем значение
    """

    while True:
        val = input(text)
        if val not in req_char:
            print(f"Значение должно лежать в {req_char}")
            continue
        return val

def get_mode(text: str, req_char: list) -> str:
    """
    Пользователь выбирает режим игры с компьютером
    :param text: Сообщение для пользователя
    :param req_char: Список допустимых значений
    :return: Выбранный пользователем уровень сложности
    """

    while True:
        val = input(text)
        if val not in req_char:
            print(f"Значение должно лежать в {req_char}")
            continue
        return val


def get_available_index_from_field(field: List[List], size: int) -> Tuple[int, int]:
    """
    Возвращает свободную ячейку для хода игрока
    :param field: Массив с записанными ходами
    :param size: Размер игрового поля
    :return: возвращает индекс строки и столбца, где делается ход игроком
    """
    while True:
        index_row = get_int_val("Введите индекс строки\n", 0, size - 1)
        index_col = get_int_val("Введите индекс столбца\n", 0, size - 1)
        if field[index_row][index_col] != EMPTY_CELL:
            print("Ячейка занята")
            continue
        return index_row, index_col


def set_player(field: List[List], current_player: str, index_row: int, index_col: int) -> List[List]:
    """

    :param field: Массив с записанными ходами
    :param current_player: Текущий игрок, который делает ход
    :param index_row: индекс строки, куда делает ход игрок
    :param index_col: индекс столбца, куда делает ход игрок
    :return: Массив с записанными ходами
    """
    field = field.copy()
    field[index_row][index_col] = current_player
    return field


def is_win(field: List[List]) -> bool:
    """
    Проверка победил ли игрок (проверка по столбцам и строкам)
    :param field: Массив с данными по ходам игроков
    :return: True - игрок победил, False - победитель ещё не выявлен
    """

    for row in field:
        if row[0] != EMPTY_CELL and all([row[0] == cell for cell in row[1:]]):
            return True
    arr_transpose = list(zip(*field))
    for row in arr_transpose:
        if row[0] != EMPTY_CELL and all([row[0] == cell for cell in row[1:]]):
            return True
    return False


def change_player(player: str) -> str:
    """
    Меняется игрок с Х на 0
    :param player: Текущий игрок
    :return: Следующий игрок
    """

    player = "X" if player == "0" else "0"
    return player


def start_player () -> int:
    """
    Определяется кто первый ходит (компьютер или игрок) для режима игры с компьютером
    :return: 0 если ходит игрок или 1 если ходит первым компьютер
    """
    draw = random.randint(0, 1) # 0 первым ходит игрок, 1 компьютер
    if draw == 0:
        print(f"По результатам жеребьёвки первым ходит игрок (Х)")
        return 0
    else:
        print(f"По результатам жеребьёвки первым ходит компьютер (Х). Игрок играет за '0'")
        return 1


def computer_step (list_of_index: List[List]):
    """
    Компьютер делает свой ход
    :param list_of_index: Список пустых ячеек для выбора своего хода
    :return: индекс строки и столбца куда компьютер делает свой ход
    """

    cell_index = random.choice(list_of_index)
    if cell_index < 10:
        index_row = 0
        index_col = cell_index
        return index_row, index_col
    else:
        index_row = cell_index // 10
        index_col = cell_index % 10
        return index_row, index_col

def game(field: List[List], player: str, size: int) -> Optional[str]:
    """
    Игра с человеком
    :param field: Массив с данными по ходам игроков
    :param player: Первый игрок
    :param size: размер игрового поля
    :return:
    """
    count_step = 0
    draw_field(field)
    max_count = size * size
    while count_step < max_count:
        print(f"Куда ставит игрок {player}")
        index_row, index_col = get_available_index_from_field(field, size)
        field = set_player(field, player, index_row, index_col)
        count_step += 1
        draw_field(field)
        if is_win(field):
            print(f"Победил игрок {player}")
            return player
        player = change_player(player)
    print("Ничья")

def game_with_computer(mode: str, field: List[List], size: int) -> Optional[str]:
    """
    Игра с компьютером
    :param mode: так скрипт понимает какой уровень сложности выбран и какой алгоритм определения хода использовать,
                нужен для будущих уровней
    :param field: Массив с данными по ходам игроков
    :param size: Размер игрового поля
    :return:
    """


    count_step = 0
    draw_field(field)
    max_count = size * size
    computer_field = start_field_for_computer(size)
    who_start = start_player()
    if who_start == 0:
        players = {"Игрок":"X", "computer":"0", "Now":"0"}
    else:
        players = {"Игрок": "0", "computer": "X", "Now":"1"}
    while count_step < max_count:
        if players["Now"] == "0":
            print(f"Ваш ход")
            index_row, index_col = get_available_index_from_field(field, size)
            field = set_player(field, players["Игрок"], index_row, index_col)
            computer_field.remove(index_row * 10 + index_col)
            count_step += 1
            draw_field(field)
            if is_win(field):
                print(f"Победил игрок")
                return "Игрок"
            players["Now"] = "1"
        else:
            print(f"Ход компьютера")
            index_row, index_col = computer_step(computer_field)
            field = set_player(field, players["computer"], index_row, index_col)
            computer_field.remove(index_row * 10 + index_col)
            count_step += 1
            draw_field(field)
            if is_win(field):
                print(f"Победил компьютер")
                return "Компьютер"
            players["Now"] = "0"
    print("Ничья")

    """
    while count_step < max_count:
        print(f"Куда ставит игрок {player}")
        index_row, index_col = get_available_index_from_field(field, size)
        field = set_player(field, player, index_row, index_col)
        count_step += 1
        draw_field(field)
        if is_win(field):
            print(f"Победил игрок {player}")
            return player
        player = change_player(player)
    print("Ничья")
"""

def app():
    """
    Запуск приложения
    :return:
    """
    size = get_int_val("Введите размер поля\n", 2, 10)
    field = init_field(size)

    flag_game = get_char_val("Какой режим? h или c\n", ["h", "c", "H", "C"])
    if flag_game in ["H", "h"]:
        player = get_char_val("Кто будет ходить первым? X или 0\n", ["X", "0"])
        game(field, player, size)
    else:
        print("В разработке")
        game_mode = get_char_val("Выберите сложность компьютера. Режим 'Удача' или 'Лёгкий'\n", ["Удача", "удача", "Лёгкий", "лёгкий", "Легкий", "легкий"])
        if game_mode in ["Лёгкий", "лёгкий", "Легкий", "легкий"]:
            print("Режим 'Лёгкий' в разработке. Будет выбран режим 'Удача'")
            game_mode = "Удача"
        game_with_computer(game_mode, field, size)
        return app()


if __name__ == "__main__":
    # f = init_field(3)
    # draw_field(f)
    # print(is_win(f))
    # f[2][0] = "X"
    # f[2][1] = "X"
    # f[2][2] = "X"
    # draw_field(f)
    # print(is_win(f))
    # print(get_int_val("Введи целое\n", 1, 3))
    # print(get_int_val("Введи целое\n"))
    app()
