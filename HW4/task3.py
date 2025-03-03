import numpy as np

# 1. Генерируем случайную квадратную матрицу размером 10x10
matrix = np.random.rand(10, 10)
print("Случайная матрица:")
print(matrix)

# 2. Находим определитель матрицы
try:
    determinant = np.linalg.det(matrix)
    if abs(determinant) < 1e-10:  # Проверка на вырожденность (определитель близок к нулю)
        print("\nМатрица вырождена (определитель близок к нулю).")
    else:
        print(f"\nОпределитель матрицы: {determinant}")
except np.linalg.LinAlgError:
    print("\nНе удалось вычислить определитель из-за ошибки линейной алгебры.")

# 3. Транспонируем матрицу
transposed_matrix = matrix.T
print("\nТранспонированная матрица:")
print(transposed_matrix)

# 4. Находим ранг матрицы
rank = np.linalg.matrix_rank(matrix)
print(f"\nРанг матрицы: {rank}")

# 5. Находим собственные значения и собственные вектора матрицы
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nСобственные значения:")
print(eigenvalues)
print("\nСобственные векторы:")
print(eigenvectors)

# 6. Генерируем вторую матрицу и выполняем операции сложения и умножения
matrix2 = np.random.rand(10, 10)
print("\nВторая случайная матрица:")
print(matrix2)

# Складываем матрицы
sum_matrix = matrix + matrix2
print("\nРезультат сложения матриц:")
print(sum_matrix)

# Умножаем матрицы
product_matrix = np.dot(matrix, matrix2)
print("\nРезультат умножения матриц:")
print(product_matrix)