import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, folder='images'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос завершился успешно

        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')

        for img in images:
            src = img.get('src')
            if not src:
                print("Отсутствует атрибут src в теге img.")
                continue

            # Создание полного URL для изображения
            src = urljoin(url, src)

            try:
                image_response = requests.get(src, stream=True)
                image_response.raise_for_status()  # Проверяем, что запрос завершился успешно
                filename = os.path.join(folder, src.split('/')[-1].split("?")[0])  # Игнорируем параметры после '?'
                with open(filename, 'wb') as f:
                    for chunk in image_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Изображение {filename} успешно сохранено.")
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при загрузке изображения {src}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Не удалось получить доступ к {url}: {e}")

# URL сайта
url = 'https://commons.wikimedia.org/wiki/Main_Page'
download_images(url)
