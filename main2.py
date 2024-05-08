import requests

# URL для API
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Печать статус-кода ответа
print("Status Code:", response.status_code)

# Печать содержимого ответа
print("Response Content:")
print(response.json())