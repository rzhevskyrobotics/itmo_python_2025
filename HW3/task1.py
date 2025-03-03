from functools import reduce

# Ввод списка чисел
numbers = [1, 2, 3, 4, 5, 6]

# 1. Создаём новый список, элементами которого будут числа из первого списка, возведенные в третью степень
cubed_numbers = list(map(lambda x: x**3, numbers))

# 2. Отбираем только чётные элементы из получившегося списка
even_numbers = list(filter(lambda x: x % 2 == 0, cubed_numbers))

# 3. Находим произведение всех элементов получившегося списка
product_of_elements = reduce(lambda x, y: x * y, even_numbers, 1)  # начальное значение 1 для пустого списка

# Выводим результаты
print("Числа, возведенные в третью степень:", cubed_numbers)
print("Четные числа из этого списка:", even_numbers)
print("Произведение всех четных чисел:", product_of_elements)