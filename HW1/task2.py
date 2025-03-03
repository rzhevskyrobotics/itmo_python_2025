# Ввод строки пользователем
user_input = input("Введите слово: ")

# Используем срез [1::2], который берет каждый второй символ, начиная с индекса 1
every_second_letter = user_input[1::2]

# Используем срез [::-1], который переворачивает строку
reversed_string = user_input[::-1]

# 1. Вывод каждой второй буквы строки
print(f"Каждая вторая буква: {every_second_letter}")

# 2. Вывод строки наоборот
print(f"Строка наоборот: {reversed_string}")