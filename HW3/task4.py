# Функция анализа данных из текстового файла
def analyze_text_file(filename):
    # Инициализируем счетчики
    line_count = 0
    word_count = 0
    char_count = 0
    longest_word = ""
    
    try:
        # Открываем файл для чтения
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Увеличиваем счетчик строк
                line_count += 1
                
                # Удаляем символы перевода строки и лишние пробелы
                clean_line = line.strip()
                
                # Подсчитываем символы в строке (без переноса строки)
                char_count += len(clean_line)
                
                # Разделяем строку на слова
                words = clean_line.split()
                word_count += len(words)
                
                # Ищем самое длинное слово
                for word in words:
                    if len(word) > len(longest_word):
                        longest_word = word

    except FileNotFoundError:
        return {"error": f"Файл '{filename}' не найден."}
    except Exception as e:
        return {"error": f"Произошла ошибка: {str(e)}"}

    # Формируем результат как словарь
    result = {
        "lines": line_count,
        "words": word_count,
        "characters": char_count,
        "longest_word": longest_word,
        "longest_word_length": len(longest_word)
    }
    return result

# Тестируем функцию
filename = "test.txt"
analysis_result = analyze_text_file(filename)
print(analysis_result)