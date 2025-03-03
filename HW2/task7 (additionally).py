# Функция для рассчёта выбранных товаров и их ценность
def knapsack(items, max_weight):
    # Преобразуем словарь в список кортежей (название, вес, ценность)
    items_list = list(items.items())
    
    # Создаем таблицу для динамического программирования
    n = len(items_list)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    # Заполняем таблицу
    for i in range(1, n + 1):
        item_name, (weight, value) = items_list[i - 1]
        for w in range(max_weight + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]  # Товар не помещается
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
    
    # Восстанавливаем выбранные товары
    result_items = {}
    total_value = dp[n][max_weight]
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Товар был взят
            item_name, (weight, value) = items_list[i - 1]
            result_items[item_name] = 1  # Количество каждого товара всегда равно 1
            w -= weight
    
    return result_items, total_value

# Исходные данные
items = {
    "laptop": (3, 1500),
    "camera": (1, 800),
    "phone": (1, 600),
    "watch": (0.5, 300),
    "headphones": (0.2, 200),
    "tablet": (2, 900),
    "wallet": (0.1, 100)
}

# Максимальный вес рюкзака
max_weight = 4

# Используем нашу функцию
selected_items, total_value = knapsack(items, max_weight)

# Вывод наших результатов
print("Выбранные товары:", selected_items)
print("Общая ценность:", total_value)