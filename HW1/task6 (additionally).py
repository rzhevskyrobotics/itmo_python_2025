# --------------------- Решение задачи вручную ---------------------

# Ввод коэффициентов
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Проверка, что a не равно 0 (иначе это не квадратное уравнение)
if a == 0:
    print("Коэффициент a не может быть равен нулю. Это не квадратное уравнение.")
else:
    # Вычисление дискриминанта
    D = b**2 - 4 * a * c

    # Анализ дискриминанта
    if D < 0:
        print("Дискриминант меньше нуля. Натуральных корней нет.")
    elif D == 0:
        # Один корень
        x = -b / (2 * a)
        if x > 0 and x.is_integer():  # Проверяем, является ли корень натуральным числом
            print(f"Единственный корень: {int(x)}")
        else:
            print("Натуральных корней нет.")
    else:
        # Два корня
        sqrt_D = D ** 0.5  # Вычисляем корень из дискриминанта
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)

        # Проверка на натуральность корней
        natural_roots = []
        if x1 > 0 and x1.is_integer():
            natural_roots.append(int(x1))
        if x2 > 0 and x2.is_integer():
            natural_roots.append(int(x2))

        if natural_roots:
            print(f"Натуральные корни: {natural_roots}")
        else:
            print("Натуральных корней нет.")

# --------------------- Решение задачи при помощи библиотек ---------------------
import math
from sympy import symbols, Eq, solve

# Ввод коэффициентов
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Проверка, что a не равно 0 (иначе это не квадратное уравнение)
if a == 0:
    print("Коэффициент a не может быть равен нулю. Это не квадратное уравнение.")
else:
    # Вычисление дискриминанта
    D = b**2 - 4 * a * c

    # Анализ дискриминанта
    if D < 0:
        print("Дискриминант меньше нуля. Натуральных корней нет.")
    elif D == 0:
        # Один корень
        x = -b / (2 * a)
        if x > 0 and x.is_integer():  # Проверяем, является ли корень натуральным числом
            print(f"Единственный корень: {int(x)}")
        else:
            print("Натуральных корней нет.")
    else:
        # Два корня
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

        # Проверка на натуральность корней
        natural_roots = []
        if x1 > 0 and x1.is_integer():
            natural_roots.append(int(x1))
        if x2 > 0 and x2.is_integer():
            natural_roots.append(int(x2))

        if natural_roots:
            print(f"Натуральные корни: {natural_roots}")
        else:
            print("Натуральных корней нет.")

    x = symbols('x')
    equation = Eq(a * x**2 + b * x + c, 0)
    solutions = solve(equation, x)
    print(f"Все корни уравнения: {solutions}")