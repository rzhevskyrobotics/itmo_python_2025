import re

# Функция для извлечения email-адресов и телефонов из текста
def get_emails_and_phones(text):
    # Прописываем регулярное выражение для email
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)

    # Прописываем регулярное выражение для телефонных номеров
    phone_pattern = r'\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
    phones = re.findall(phone_pattern, text)

    return emails, phones

# Основная функция программы
def process_file(input_filename, output_filename):
    try:
        # Читаем содержимое файла
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Извлекаем email-адреса и номера телефонов
        emails, phones = get_emails_and_phones(content)

        # Записываем результаты в выходной файл
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write("Найденные email-адреса:\n")
            for email in emails:
                output_file.write(f"{email}\n")

            output_file.write("\nНайденные телефонные номера:\n")
            for phone in phones:
                output_file.write(f"{phone}\n")

        print(f"Данные успешно сохранены в файл '{output_filename}'.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запускаем нашу программу и используем функцию
if __name__ == "__main__":
    input_file = "input_data.txt"
    output_file = "output_data.txt"

    process_file(input_file, output_file)