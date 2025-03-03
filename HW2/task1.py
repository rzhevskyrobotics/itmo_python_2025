# Даны списки
list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']

# Объединение списков поочередно через генератор списка
result = [item for pair in zip(list_1, list_2) for item in pair]

# Выводим результат
print(result)