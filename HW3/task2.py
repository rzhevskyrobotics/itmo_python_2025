# Функция проверки числа на простое
def is_prime(n):
    # Числа меньше или равные 1 не являются простыми
    if n <= 1:
        return False
    
    # Проверяем делители от 2 до sqrt(n)
    for i in range(2, int(n**0.5) + 1):  # Достаточно проверить до корня из n
        if n % i == 0:  # Если n делится на i без остатка, то оно не простое
            return False
    
    # Если никаких делителей не найдено, число простое
    return True

# Проверяем работу функции
numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20]
results = {num: is_prime(num) for num in numbers}
print(results)