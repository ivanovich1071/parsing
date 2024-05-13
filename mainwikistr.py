from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    # Настройка драйвера
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

    def perform_new_search():
        # Функция для выполнения нового поиска
        initial_query = input("Введите поисковый запрос: ")
        search_box = browser.find_element(By.ID, "searchInput")
        search_box.clear()
        search_box.send_keys(initial_query + Keys.RETURN)
        visited_links.append(browser.current_url)

    # Список для хранения посещенных страниц
    visited_links = []

    # Получаем запрос от пользователя
    perform_new_search()

    while True:
        action = input("Выберите действие: 1 - листать параграфы, 2 - перейти на связанную страницу, 3 - выйти: ")

        if action == "1":
            # Листаем параграфы текущей статьи
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            reading = True
            while reading:
                for paragraph in paragraphs:
                    print(paragraph.text)
                    user_input = input("Нажмите Enter для продолжения чтения или введите 7 для выхода: ")
                    if user_input.lower() == "7":
                        while True:
                            esc_action = input(
                                "Выберите: 1 - новый поиск, 2 - вернуться к начальному поиску, 3 - выход: ")
                            if esc_action == "1":
                                perform_new_search()
                                reading = False
                                break
                            elif esc_action == "2":
                                browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
                                perform_new_search()
                                reading = False
                                break
                            elif esc_action == "3":
                                browser.quit()
                                return
                        if not reading:
                            break
                if not reading:
                    break

        elif action == "2":
            # Показываем список связанных страниц
            links = browser.find_elements(By.CSS_SELECTOR,
                                          "#mw-content-text [href^='/wiki/']:not([href*='redlink']):not([href*=':'])")
            for i, link in enumerate(links[:10]):  # Покажем первые 10 ссылок
                print(f"{i + 1}: {link.text} ({link.get_attribute('href')})")

            link_choice = input(
                f"Выберите страницу от 1 до {min(10, len(links))} для перехода или введите 0 для отмены: ")
            if link_choice.isdigit() and 0 < int(link_choice) <= min(10, len(links)):
                # Прокручиваем страницу к выбранному элементу, чтобы он был видимым
                browser.execute_script("arguments[0].scrollIntoView(true);", links[int(link_choice) - 1])
                # Ждем, пока элемент станет интерактивным
                time.sleep(1)
                # Кликаем на выбранный элемент
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

