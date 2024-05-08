import requests

# URL для API GitHub 
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    'q': 'language:html'
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Печать статус-кода ответа
print("Status Code:", response.status_code)

# Печать содержимого ответа в JSON-формате
print("Response JSON:")
print(response.json())