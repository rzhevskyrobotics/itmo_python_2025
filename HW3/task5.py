# Функция объединения содержимого нескольких текстовых файлов
def merge_files(file_paths, write_to_file=True, output_file="merged_output.txt"):
    """
    Функция для объединения содержимого нескольких текстовых файлов.

    :param file_paths: Список строк с путями к файлам.
    :param write_to_file: Флаг для записи результата в файл (по умолчанию True).
    :param output_file: Имя выходного файла, если write_to_file=True.
    :return: Объединенная строка с содержимым всех файлов.
    """
    merged_content = ""

    # Читаем содержимое каждого файла
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                merged_content += file.read() + "\n"  # Добавляем перенос строки между файлами
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except Exception as e:
            print(f"Ошибка при чтении файла {file_path}: {e}")

    # Удаляем последний лишний перенос строки
    merged_content = merged_content.rstrip("\n")

    # Записываем в файл, если указан флаг True
    if write_to_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(merged_content)
            print(f"Содержимое успешно записано в файл: {output_file}")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

    return merged_content


# Выполняем нашу функцию
if __name__ == "__main__":
    
    file_list = ['input1.txt', 'input2.txt', 'input3.txt']
    
    result = merge_files(file_list)
    print(f"Объединённое содержимое: {result}")

    # Вызываем функцию, но ставим флаг без записи в файл
    result_no_write = merge_files(file_list, write_to_file=False)
    print(f"Объединённое содержимое (без записи): {result_no_write}")