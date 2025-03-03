import os
import shutil
import time
from datetime import datetime

def create_backup(source_dir, target_dir):
    """
    Функция для создания резервной копии.
    :param source_dir: Исходная директория для резервного копирования.
    :param target_dir: Целевая директория для хранения резервных копий.
    """
    # Создаем имя новой папки в формате "YYYY-MM-DD_HH-MM-SS"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = os.path.join(target_dir, timestamp)

    # Создаем новую папку для резервной копии
    os.makedirs(backup_folder, exist_ok=True)

    # Рекурсивно копируем все файлы и поддиректории из исходной директории в целевую
    try:
        shutil.copytree(source_dir, os.path.join(backup_folder, os.path.basename(source_dir)))
        print(f"Резервная копия успешно создана: {backup_folder}")
    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")

# Основная функция
def main():
    print("Программа резервного копирования.")
    
    # 1: Пользователь указывает исходную директорию
    source_dir = input("Введите путь к исходной директории: ").strip()
    if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
        print("Указанная исходная директория не существует или некорректна.")
        return

    # 2: Пользователь указывает целевую директорию
    target_dir = input("Введите путь к целевой директории для резервных копий: ").strip()
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        print(f"Целевая директория создана: {target_dir}")

    # 3: Установка интервала между резервными копиями
    try:
        interval_minutes = int(input("Введите интервал между резервными копиями (в минутах): "))
        if interval_minutes <= 0:
            raise ValueError
    except ValueError:
        print("Некорректный интервал. Используется значение по умолчанию: 10 минут.")
        interval_minutes = 10

    interval_seconds = interval_minutes * 60

    print("Для завершения работы программы нажмите Ctrl+C или введите 'exit'.")
    
    # Основной цикл для создания резервных копий
    try:
        while True:
            create_backup(source_dir, target_dir)
            print(f"Следующая резервная копия будет создана через {interval_minutes} минут(-ы).")
            
            # Проверяем ввод пользователя каждую секунду
            for _ in range(interval_seconds):
                time.sleep(1)
                if input(">>> ").strip().lower() == "exit":
                    print("Программа завершает работу.")
                    return
    except KeyboardInterrupt:
        print("\nПрограмма завершена по запросу пользователя.")

# Запускаем нашу программу
if __name__ == "__main__":
    main()