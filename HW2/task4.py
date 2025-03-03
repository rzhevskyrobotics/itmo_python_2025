# Функция для инвертирования словаря
def invert_dict(input_dict):
    # Создаем новый словарь, где значения становятся ключами, а ключи — значениями
    inverted_dict = {value: key for key, value in input_dict.items()}
    return inverted_dict

# Применяем нашу функцию
input_dict = {'key1': 'value1', 'key2': 'value2', 'key3':'value3'}
result = invert_dict(input_dict)
print(result)