import pandas as pd
import numpy as np
from zipfile import ZipFile
from sqlalchemy import create_engine

# 1. Скачмваем архив по ссылке и разархивируем его при помощи zipfile
archive_path = 'recipes.zip'  # Путь к скачанному архиву
with ZipFile(archive_path, 'r') as zip_ref:
    zip_ref.extractall('extracted_recipes')  # Распаковываем файлы в папку extracted_recipes

# 2. Считаем первый файл из архива при помощи pandas
first_file = 'recipes.csv'  # Первый файл из архива
recipes_df = pd.read_csv(f'extracted_recipes/{first_file}')

# 3. Выводим типы данных столбцов
print("Типы данных столбцов:")
print(recipes_df.dtypes)

# 4. Находим максимум в столбце n_steps
max_n_steps = recipes_df['n_steps'].max()
print(f"Максимум в столбце n_steps: {max_n_steps}")

# 5. Считаем количество отзывов с группировкой по месяцам добавления отзыва в базу
recipes_df['submitted_month'] = pd.to_datetime(recipes_df['submitted']).dt.to_period('M')
reviews_by_month = recipes_df.groupby('submitted_month').size()
print("Количество отзывов по месяцам:")
print(reviews_by_month)

# 6. Находим пользователя, отправлявшего рецепты чаще всех
most_active_user = recipes_df['contributor_id'].mode()[0]
print(f"Самый активный пользователь (contributor_id): {most_active_user}")

# 7. Находим самый первый и самый последний по дате отправления рецепт
recipes_df['submitted'] = pd.to_datetime(recipes_df['submitted'])
earliest_recipe = recipes_df.loc[recipes_df['submitted'].idxmin()]
latest_recipe = recipes_df.loc[recipes_df['submitted'].idxmax()]
print("Самый ранний рецепт:")
print(earliest_recipe[['id', 'name', 'submitted']])
print("Самый поздний рецепт:")
print(latest_recipe[['id', 'name', 'submitted']])

# 8. Определяем медианы по количеству ингредиентов и по времени приготовления
median_n_ingredients = recipes_df['n_ingredients'].median()
median_minutes = recipes_df['minutes'].median()
print(f"Медиана количества ингредиентов: {median_n_ingredients}")
print(f"Медиана времени приготовления: {median_minutes}")

# 9. Находим самый простой рецепт
simplest_recipe = recipes_df.loc[
    (recipes_df['n_ingredients'] == recipes_df['n_ingredients'].min()) &
    (recipes_df['minutes'] == recipes_df['minutes'].min()) &
    (recipes_df['n_steps'] == recipes_df['n_steps'].min())
]
print("Самый простой рецепт:")
print(simplest_recipe[['id', 'name', 'n_ingredients', 'minutes', 'n_steps']])

# 10. Загружаем рецепты в базу данных SQLite
engine = create_engine('sqlite:///recipes.db')
recipes_df.to_sql('recipes', con=engine, if_exists='replace', index=False)
print("Данные успешно загружены в базу данных SQLite.")

# 11. Берём рецепты, у которых время приготовления меньше медианы и количество шагов меньше среднего
filtered_recipes = recipes_df[
    (recipes_df['minutes'] < median_minutes) & (recipes_df['n_steps'] < recipes_df['n_steps'].mean())
]

# 12. Сохраняем полученный датафрейм в файл .csv
filtered_recipes.to_csv('filtered_recipes.csv', index=False)
print("Отфильтрованные рецепты сохранены в файл filtered_recipes.csv.")