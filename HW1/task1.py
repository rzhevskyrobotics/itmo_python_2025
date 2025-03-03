# Ввод переменных x и y
x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))

# Выполнение арифметических операций
sum_result = x + y
difference_result = x - y
product_result = x * y
division_result = x / y if y != 0 else "Невозможно (деление на ноль)"
remainder_result = x % y if y != 0 else "Невозможно (деление на ноль)"
power_result = x ** y

# Результаты
print(f"Сумма x и y: {x} + {y} = {sum_result}")
print(f"Разность x и y: {x} - {y} = {difference_result}")
print(f"Произведение x и y: {x} * {y} = {product_result}")
print(f"Деление x на y: {x} / {y} = {division_result}")
print(f"Остаток от деления x на y: {x} % {y} = {remainder_result}")
print(f"x в степени y: {x} ^ {y} = {power_result}")