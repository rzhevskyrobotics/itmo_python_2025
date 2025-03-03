import dask.dataframe as dd
from zipfile import ZipFile
from sqlalchemy import create_engine

# 1. Считываем все файлы из архива
archive_path = 'recipes.zip'  # Путь к скачанному архиву
with ZipFile(archive_path, 'r') as zip_ref:
    zip_ref.extractall('extracted_recipes')  # Распаковываем файлы в папку extracted_recipes

# Считываем все CSV-файлы из папки с помощью Dask
recipes_ddf = dd.read_csv('extracted_recipes/*.csv')

# 2. Выводим метаинформацию о таблице: npartitions и типы столбцов
print(f"Количество партиций (npartitions): {recipes_ddf.npartitions}")
print("Типы столбцов:")
print(recipes_ddf.dtypes)

# 3. Выводим на экран 5 первых строк таблицы
try:
    print("Первые 5 строк таблицы:")
    print(recipes_ddf.head().compute())
except Exception as e:
    print(f"Ошибка: {e}")
    print("Причина ошибки: возможно, не все столбцы имеют одинаковый тип данных или есть пропущенные значения.")
    # явно указываем типы данных при чтении
    recipes_ddf = dd.read_csv('extracted_recipes/*.csv', dtype={'id': 'int64', 'minutes': 'float64', 'n_steps': 'float64', 'n_ingredients': 'float64'})
    print("Первые 5 строк после исправления:")
    print(recipes_ddf.head().compute())

try:
    print("Последние 5 строк таблицы:")
    print(recipes_ddf.tail().compute())  # .tail() возвращает последние строки
except Exception as e:
    print(f"Ошибка: {e}")
    print("Причина ошибки: аналогично предыдущей ошибке.")

# 4. Считаем, сколько строк содержит каждый из блоков
partition_sizes = recipes_ddf.map_partitions(len).compute()
print("Количество строк в каждом блоке:")
print(partition_sizes)

# 5. Находим максимум в столбце n_steps
max_n_steps = recipes_ddf['n_steps'].max()
print(f"Максимум в столбце n_steps: {max_n_steps.compute()}")

# 6. Визуализируем граф вычислений
max_n_steps.visualize(filename='max_n_steps_graph', format='png')
print("Граф вычислений сохранен в файл max_n_steps_graph.png")

# 7. Считаем количество отзывов с группировкой по месяцам добавления отзыва в базу
recipes_ddf['submitted_month'] = dd.to_datetime(recipes_ddf['submitted']).dt.to_period('M')
reviews_by_month = recipes_ddf.groupby('submitted_month').size().compute()
print("Количество отзывов по месяцам:")
print(reviews_by_month)

# 8. Находим пользователя, отправлявшего рецепты чаще всех
most_active_user = recipes_ddf['contributor_id'].value_counts().idxmax().compute()
print(f"Самый активный пользователь (contributor_id): {most_active_user}")

# 9. Находим самый первый и самый последний по дате отправления рецепт
recipes_ddf['submitted'] = dd.to_datetime(recipes_ddf['submitted'])
earliest_recipe = recipes_ddf.loc[recipes_ddf['submitted'].idxmin().compute()]
latest_recipe = recipes_ddf.loc[recipes_ddf['submitted'].idxmax().compute()]
print("Самый ранний рецепт:")
print(earliest_recipe.compute()[['id', 'name', 'submitted']])
print("Самый поздний рецепт:")
print(latest_recipe.compute()[['id', 'name', 'submitted']])

# 10. Загружаем рецепты в базу данных SQLite
engine = create_engine('sqlite:///recipes.db')
recipes_ddf.compute().to_sql('recipes', con=engine, if_exists='replace', index=False)
print("Данные успешно загружены в базу данных SQLite.")

# 11. Выбираем рецепты, у которых время приготовления меньше медианы и количество шагов меньше среднего
median_minutes = recipes_ddf['minutes'].quantile(0.5).compute()
mean_n_steps = recipes_ddf['n_steps'].mean().compute()

filtered_recipes = recipes_ddf[
    (recipes_ddf['minutes'] < median_minutes) & (recipes_ddf['n_steps'] < mean_n_steps)
].compute()

# 12. Сохраняем полученный датафрейм в файл .csv
filtered_recipes.to_csv('filtered_recipes.csv', index=False)
print("Отфильтрованные рецепты сохранены в файл filtered_recipes.csv.")