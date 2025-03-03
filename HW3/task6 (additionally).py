def my_hash(s: str, table_size: int = 256) -> int:
    """
    Хеш-функция для преобразования строки в индекс.
    :param s: Входная строка.
    :param table_size: Размерность таблицы (по умолчанию 256).
    :return: Индекс для размещения строки.
    """
    hash_value = ''.join(format(ord(c), '03d') for c in s)  # Преобразуем каждый символ в его юникод
    return int(hash_value) % table_size

def add_to_table(table: dict, s: str, index: int) -> dict:
    """
    Добавление строки в хеш-таблицу.
    :param table: Словарь (хеш-таблица).
    :param s: Строка для добавления.
    :param index: Индекс, полученный с помощью my_hash.
    :return: Обновленная хеш-таблица.
    """
    if index not in table:
        table[index] = []  # Инициализируем список для данного индекса

    if s in table[index]:
        print(f"Строка '{s}' уже существует в таблице.")
    else:
        table[index].append(s)
        print(f"Строка '{s}' успешно добавлена в таблицу.")

    return table

def remove_from_table(table: dict, s: str, index: int) -> dict:
    """
    Удаление строки из хеш-таблицы.
    :param table: Словарь (хеш-таблица).
    :param s: Строка для удаления.
    :param index: Индекс, полученный с помощью my_hash.
    :return: Обновленная хеш-таблица.
    """
    if index not in table:
        print(f"Индекс {index} отсутствует в таблице.")
        return table

    if s not in table[index]:
        print(f"Строка '{s}' не найдена в таблице.")
    else:
        table[index].remove(s)
        print(f"Строка '{s}' успешно удалена из таблицы.")
        if not table[index]:  # Если список пуст, удаляем ключ
            del table[index]

    return table

def search_in_table(table: dict, s: str, index: int) -> tuple or bool:
    """
    Поиск строки в хеш-таблице.
    :param table: Словарь (хеш-таблица).
    :param s: Строка для поиска.
    :param index: Индекс, полученный с помощью my_hash.
    :return: Кортеж (ключ словаря, индекс в списке) или False, если строка не найдена.
    """
    if index not in table:
        print(f"Индекс {index} отсутствует в таблице.")
        return False

    if s in table[index]:
        position = table[index].index(s)
        print(f"Строка '{s}' найдена в индексе {index}, позиция в списке: {position}.")
        return index, position
    else:
        print(f"Строка '{s}' не найдена в таблице.")
        return False

# Консольный интерфейс
def main():
    hash_table = {}  # Инициализация пустой хеш-таблицы
    table_size = 256  # Размерность таблицы

    # Заполнение таблицы начальными значениями
    initial_strings = ["apple", "banana", "cherry", "date", "elderberry"]
    for string in initial_strings:
        idx = my_hash(string, table_size)
        add_to_table(hash_table, string, idx)

    while True:
        print("\nМеню:")
        print("1. Добавить строку")
        print("2. Удалить строку")
        print("3. Найти строку")
        print("4. Показать таблицу")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            string = input("Введите строку для добавления: ")
            idx = my_hash(string, table_size)
            hash_table = add_to_table(hash_table, string, idx)

        elif choice == "2":
            string = input("Введите строку для удаления: ")
            idx = my_hash(string, table_size)
            hash_table = remove_from_table(hash_table, string, idx)

        elif choice == "3":
            string = input("Введите строку для поиска: ")
            idx = my_hash(string, table_size)
            result = search_in_table(hash_table, string, idx)

        elif choice == "4":
            print("Текущее состояние таблицы:")
            for key, value in hash_table.items():
                print(f"Индекс {key}: {value}")

        elif choice == "5":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

# И проверяем функции через консольный интерфейс
if __name__ == "__main__":
    main()