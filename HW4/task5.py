import random
import string

# Функция для генерации случайного пароля
def generate_password(length):
    if length < 4:
        print("Длина пароля должна быть не менее 4 символов для обеспечения минимальной безопасности.")
        return None

    # Определяем набор символов для пароля
    lowercase_letters = string.ascii_lowercase  # Буквы в нижнем регистре
    uppercase_letters = string.ascii_uppercase  # Буквы в верхнем регистре
    digits = string.digits                      # Цифры
    special_characters = string.punctuation     # Специальные символы

    # Объединяем все символы в один набор
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Убедимся, что пароль содержит хотя бы по одному символу каждого типа
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Заполняем остальную часть пароля случайными символами
    password += random.choices(all_characters, k=length - 4)

    # Перемешиваем символы, чтобы порядок был случайным
    random.shuffle(password)

    # Преобразуем список символов в строку
    return ''.join(password)

# Запускаем нашу программу
if __name__ == "__main__":
    try:
        length = int(input("Введите длину пароля: "))
        password = generate_password(length)
        if password:
            print(f"Сгенерированный пароль: {password}")
    except ValueError:
        print("Пожалуйста, введите целое число для длины пароля.")