# Функция для создания нового списка после переработанного
def own_map(func, iterable):
    # Проверяем, что второй аргумент является итерируемым объектом
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' объект не поддается итерации")
    
    # Создаем новый список с применением функции func к каждому элементу iterable
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# Используем нашу функцию
numbers = [1, 2, 3, 4, 5]

# Функция для возведения чисел в квадрат
def square(x):
    return x ** 2

squared_numbers = own_map(square, numbers)
print(squared_numbers)

# Используем нашу функцию с лямбда-функцией
doubled_numbers = own_map(lambda x: x * 2, numbers)
print(doubled_numbers)