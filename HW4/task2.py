import requests

# Функция для получения информации о пользователе
def get_github_user_info(username):
    # URL API GitHub
    url = f"https://api.github.com/users/{username}"
    
    try:
        # Отправляем GET-запрос к API
        response = requests.get(url)
        
        # Проверяем, был ли запрос успешным (статус код 200)
        if response.status_code == 200:
            # Получаем данные в формате JSON
            user_data = response.json()
            
            # Извлекаем необходимые данные
            name = user_data.get('name', 'Не указано')
            login = user_data.get('login', 'Не указано')
            repo_count = user_data.get('public_repos', 0)
            
            # Выводим информацию на экран
            print(f"Имя пользователя: {name}")
            print(f"Логин: {login}")
            print(f"Количество публичных репозиториев: {repo_count}")
        elif response.status_code == 404:
            print(f"Пользователь с логином '{username}' не найден.")
        else:
            print(f"Произошла ошибка при запросе. Код ошибки: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")

# Запускаем нашу программу
if __name__ == "__main__":
    username = input("Введите имя пользователя GitHub: ")
    get_github_user_info(username)