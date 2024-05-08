import os
import requests
from bs4 import BeautifulSoup

def download_images(url, folder='images'):
    # Создание папки, если она не существует
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Получение HTML-контента страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Поиск всех тегов img и извлечение атрибутов src
    images = soup.find_all('img')
    for img in images:
        src = img.get('src')
        if src:
            # Проверка, что src ссылается на изображение
            if not src.startswith(('http://', 'https://')):
                src = url + '/' + src
            image_response = requests.get(src, stream=True)
            if image_response.status_code == 200:
                # Извлечение имени файла из URL
                filename = os.path.join(folder, src.split('/')[-1])
                # Сохранение изображения в файл
                with open(filename, 'wb') as f:
                    for chunk in image_response:
                        f.write(chunk)

# URL сайта, с которого будут загружаться изображения
url = 'https://illarionov-marketig.ru'
download_images(url)