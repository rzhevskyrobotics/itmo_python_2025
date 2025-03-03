# ------------------- Простой вариант -------------------
def Determinant_3x3(matrix):
    # Проверка, что матрица имеет размер 3x3
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Матрица должна быть размера 3x3")
    
    # Извлекаем элементы матрицы
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    # Вычисляем определитель
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

# И используем нашу функцию
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Определитель матрицы 3x3:", Determinant_3x3(matrix))

# ------------------- Сложный вариант -------------------
def determinant(matrix):
    # Проверяем, что матрица является квадратной
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    # Базовый случай: если матрица 1x1, возвращаем единственный элемент
    if n == 1:
        return matrix[0][0]
    
    # Базовый случай: если матрица 2x2, используем простую формулу
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Разложение по первой строке
    det = 0
    for j in range(n):
        # Создаем подматрицу, удаляя первую строку и j-й столбец
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        
        # Рекурсивно вычисляем определитель подматрицы
        sign = (-1) ** j  # Знак для текущего элемента
        det += sign * matrix[0][j] * determinant(sub_matrix)
    
    return det


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Определитель матрицы n×n:", determinant(matrix))

# ------------------- Библиотечный вариант (numpy) -------------------
import numpy as np

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Преобразуем список списков в массив NumPy
np_matrix = np.array(matrix)

# Вычисляем определитель
det = np.linalg.det(np_matrix)

# Вывод округляем для читаемости
print("Определитель с помощью NumPy:", round(det, 6))