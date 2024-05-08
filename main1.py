import requests

# URL для API
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    'userId': 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверяем, успешен ли запрос
if response.status_code == 200:
    # Выводим полученные записи
    posts = response.json()  # Преобразуем ответ из JSON
    for post in posts:
        print(f"Post ID: {post['id']}, Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print("Failed to fetch data:", response.status_code)