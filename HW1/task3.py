# Создаем пустой список для хранения чисел
numbers = []

# Цикл для ввода чисел до тех пор, пока не будет введено -1
while True:
    user_input = int(input("Введите число (или -1 для завершения): "))
    if user_input == -1:  # Проверка на условие выхода для завершения
        break
    numbers.append(user_input)  # Добавляем число в список

# Считаем сумму элементов через цикл
sum_via_loop = 0
for num in numbers:
    sum_via_loop += num

# Считаем сумму элементов метод списка - sum()
sum_via_method = sum(numbers)

# Считаем только четные элементы списка
even_numbers = [num for num in numbers if num % 2 == 0]

# 1. Вывод длины списка
print(f"Длина списка: {len(numbers)}")

# 2. Вывод суммы элементов через цикл
print(f"Сумма элементов через цикл: {sum_via_loop}")

# 3. Вывод суммы элементов через метод списка
print(f"Сумма элементов через метод sum(): {sum_via_method}")

# 4. Вывод только четных элементов списка
print(f"Четные элементы списка: {even_numbers}")