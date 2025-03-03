import string

# Строка
s = "Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде."

# 1. Устанавлиаем все слова к нижнему регистру
s_lower = s.lower()

# 2. Очищаем строки от знаков препинания
# Создаем перевод таблицу для замены знаков препинания на пустые символы
translator = str.maketrans('', '', string.punctuation + '—«»')
s_clean = s_lower.translate(translator)

# 3. Создаём список слов
words_list = s_clean.split()

# 4. Создаём словарь с подсчетом частоты слов
word_count = {}
for word in words_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Сортируем словарь по значениям в порядке убывания
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

# Вывод наших результатов
print("Список слов:", words_list)
print("\nЧастотный словарь (отсортированный):")
for word, count in sorted_word_count.items():
    print(f"{word}: {count}")