from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def search_wikipedia():
    # Настройка драйвера
    driver = webdriver.Chrome()  # Укажите путь к драйверу, если необходимо
    driver.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

    visited_links = []

    while True:
        # Запрос поисковой фразы от пользователя
        query = input("Введите запрос для поиска в Википедии или 'выход' для завершения программы: ")
        if query.lower() == 'выход':
            break

        # Ввод запроса в строку поиска и отправка формы
        search_box = driver.find_element(By.NAME, "search")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Сохранение текущей ссылки
        current_url = driver.current_url
        visited_links.append(current_url)

        while True:
            action = input(
                "Выберите действие: \na) Пролистать параграфы\nb) Просмотреть связанные страницы\nc) Выйти\n> ")

            if action.lower() == 'a':
                paragraphs = driver.find_elements(By.CSS_SELECTOR, 'p')
                for para in paragraphs:
                    input(f"{para.text}\n\n(Нажмите Enter для продолжения, 'esc' для выхода)")
                    if input() == 'esc':
                        break

            elif action.lower() == 'b':
                related_links = driver.find_elements(By.CSS_SELECTOR, '#mw-normal-catlinks a')
                for i, link in enumerate(related_links[:10]):
                    print(f"{i + 1}: {link.text} - {link.get_attribute('href')}")

                # Выбор статьи для детального просмотра
                link_number = int(input("Введите номер связанной страницы для перехода: "))
                related_links[link_number - 1].click()

                # Обновление текущей ссылки
                current_url = driver.current_url
                visited_links.append(current_url)

                # Возврат к выбору действий
                continue

            elif action.lower() == 'c':
                print("Завершение программы. Посещенные страницы:")
                for link in visited_links:
                    print(link)
                driver.quit()
                return


search_wikipedia()