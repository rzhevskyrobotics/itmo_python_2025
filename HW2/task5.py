# Функция нахождения пересечения множеств
def find_intersection(list_of_sets):
    # Проверяем, что список не пустой
    if not list_of_sets:
        return set()  # Если список пуст, возвращаем пустое множество
    
    # Используем первый элемент списка как начальное множество для пересечения
    result = list_of_sets[0]
    
    # Находим пересечение с остальными множествами
    for current_set in list_of_sets[1:]:
        result = result.intersection(current_set)
    
    return result

# Используем нашу функцию
list_of_sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
result = find_intersection(list_of_sets)
print(result)