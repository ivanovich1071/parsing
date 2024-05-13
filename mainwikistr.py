from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    # Настройка драйвера
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

    # Список для хранения посещенных страниц
    visited_links = []

    # Получаем запрос от пользователя
    initial_query = input("Введите поисковый запрос: ")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(initial_query + Keys.RETURN)

    # Добавляем текущую ссылку в список посещенных
    visited_links.append(browser.current_url)

    while True:
        action = input("Выберите действие: 1 - листать параграфы, 2 - перейти на связанную страницу, 3 - выйти: ")

        if action == "1":
            # Листаем параграфы текущей статьи
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                input("Нажмите Enter для продолжения чтения...")

        elif action == "2":
            # Показываем список связанных страниц
            links = browser.find_elements(By.CSS_SELECTOR,
                                          "#mw-content-text [href^='/wiki/']:not([href*='redlink']):not([href*=':'])")
            for i, link in enumerate(links[:10]):  # Покажем первые 10 ссылок
                print(f"{i + 1}: {link.text} ({link.get_attribute('href')})")

            link_choice = input(
                f"Выберите страницу от 1 до {min(10, len(links))} для перехода или введите 0 для отмены: ")
            if link_choice.isdigit() and 0 < int(link_choice) <= min(10, len(links)):
                links[int(link_choice) - 1].click()
                visited_links.append(browser.current_url)
                time.sleep(2)  # Даем время странице для загрузки

        elif action == "3":
            # Выводим посещенные ссылки и выходим
            print("Посещенные страницы:")
            for link in visited_links:
                print(link)
            break

    browser.quit()


if __name__ == "__main__":
    main()