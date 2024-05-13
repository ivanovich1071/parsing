from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

# Создаем экземпляр браузера
browser = webdriver.Chrome()

# Заходим на главную страницу русской Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем по заголовку, что это действительно Википедия
assert "Википедия" in browser.title

# Ждем 5 секунд
time.sleep(5)

# Находим поле поиска по его ID
search_box = browser.find_element(By.ID, "searchInput")

# Вводим текст "Солнечная система" и отправляем запрос
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)

# Ждем 30 секунд, чтобы страница загрузилась
time.sleep(30)

# Собираем все элементы с тегом 'div'
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    # Получаем класс элемента
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

# Если список hatnotes не пуст, выбираем случайный элемент и переходим по ссылке
if hatnotes:
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)

# Закрываем браузер
browser.quit()
print(hatnotes)