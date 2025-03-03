from datetime import datetime

# Принимаем дату рождения от пользователя
day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения: "))
year = int(input("Введите год вашего рождения: "))

# 1. Определение квартала
if 1 <= month <= 3:
    quarter = "первом квартале"
elif 4 <= month <= 6:
    quarter = "втором квартале"
elif 7 <= month <= 9:
    quarter = "третьем квартале"
else:
    quarter = "четвертом квартале"

# Проверяем на високосный год
is_leap_year = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap_year = True

# Расчет количества дней с момента рождения
# Текущая дата
current_date = datetime.now()
# Дата рождения
birth_date = datetime(year, month, day)

# Разница между текущей датой и датой рождения
delta = current_date - birth_date

# Количество дней с учетом средней длины года в 365.25 дней
average_days_since_birth = delta.days + (current_date.hour / 24) + (current_date.minute / 1440)

# 1. Выводим квартал года рождения
print(f"Вы родились в {quarter} года.")

# 2. Выводим был ли год рождения пользователя весокосным
if is_leap_year:
    print(f"{year} - год вашего рождения является високосным.")
else:
    print(f"{year} - год вашего рождения не является високосным.")

# 3. Выводим количество дней с момента рождения пользователя
print(f"С момента вашего рождения прошло примерно {average_days_since_birth:.2f} дней.")