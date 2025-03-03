# Определяем исходный список кортежей
persons = [('Elena', 34), ('Alex', 13), ('John', 21)]

# Фильтрация и сортировка списка
result = sorted(
    [person for person in persons if person[1] > 18],  # Фильтруем возраст > 18
    key=lambda x: x[1],                                # Сортируем по возрасту
    reverse=True                                       # Устанавливаем сортировку в порядке убывания
)

# Выводим результат
print(result)