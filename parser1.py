import requests
from bs4 import BeautifulSoup
import wget
import os

# URL сайта для парсинга
url = 'https://www.iloveimg.com/ru'

# Отправляем запрос к сайту
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ссылки на странице
links = soup.find_all('a')

# Список для хранения ссылок на PDF файлы
pdf_links = []

# Перебираем все найденные ссылки
for link in links:
    href = link.get('href')
    if href is not None and href.endswith('.pdf'):
        pdf_links.append(href)
        # Скачиваем PDF файл
        if not os.path.exists('pdf_files'):
            os.makedirs('pdf_files')
        wget.download(href, out='pdf_files')

# Сохраняем информацию о скачанных PDF файлах в текстовом файле
with open('pdf_files_info.txt', 'w') as file:
    file.write('Список скачанных PDF файлов:\n\n')
    for pdf_link in pdf_links:
        file.write(pdf_link + '\n')

# Функция проверки наличия текстовой информации
def check_text_content(soup):
    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])
    if not text_elements:
        return False
    for element in text_elements:
        if element.get_text(strip=True):  # Проверка, что элемент содержит текст
            return True
    return False

# Проверяем наличие текстовой информации на сайте
has_text_content = check_text_content(soup)
if has_text_content:
    print("Текстовая информация найдена на сайте.")
else:
    print("Текстовая информация на сайте не найдена.")

# Находим все текстовые элементы на странице (например, абзацы, заголовки)
text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])

# Список для хранения текстовой информации
text_data = []

# Извлекаем текст из всех найденных элементов и сохраняем его
for element in text_elements:
    text = element.get_text()
    text_data.append(text)

# Сохраняем текстовую информацию в файл
with open('text_data.txt', 'w', encoding='utf-8') as file:
    file.write('Текстовая информация с сайта:\n\n')
    for text_item in text_data:
        file.write(text_item + '\n')

    file.write('\nСписок скачанных PDF файлов:\n\n')
    for pdf_link in pdf_links:
        file.write(pdf_link + '\n')

print("Информация успешно сохранена в файл text_data.txt.")