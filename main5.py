import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка драйвера
driver = webdriver.Chrome()
url = "https://www.21vek.by/canes_crutches_walkers/26_aversus_04.html"
driver.get(url)
time.sleep(3)

# Заголовки для CSV файла
csv_headers = ["Наименование товара", "Цена"]

# Открываем CSV файл для записи
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)  # Записываем заголовки

    # Используем метод find_elements с By.CLASS_NAME для карточек товара
    cards = driver.find_elements(By.CLASS_NAME, 'style_containerImg__PRUiL')

    for card in cards:
        # Получаем наименование товара
        try:
            product_name = card.find_element(By.XPATH, './/img').get_attribute('alt')
        except:
            product_name = "Не удалось найти наименование"

        # Получаем цену товара
        try:
            price_element = driver.find_element(By.CLASS_NAME, 'ProductPrice_productPrice__thjM7')
            price = price_element.text.replace('<!-- -->', '')
        except:
            price = "Не удалось найти цену"

        # Печатаем и записываем данные в CSV файл
        print(f"Наименование товара: {product_name}, Цена: {price}")
        writer.writerow([product_name, price])

# Закрыть драйвер
driver.quit()
