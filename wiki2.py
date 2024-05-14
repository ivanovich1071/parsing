from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def initialize_driver():
    driver = webdriver.Chrome()
    return driver


def search_wikipedia(driver, query):
    driver.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    time.sleep(2)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)


def get_paragraphs(driver):
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    return [p.text for p in paragraphs if p.text]


def print_paragraphs(driver):
    paragraphs = get_paragraphs(driver)
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}:\n{paragraph}\n")
        user_input = input("Нажмите Enter для продолжения или 'esc' для выхода: ").strip().lower()
        if user_input == 'esc':
            break


def get_related_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "#mw-content-text .mw-parser-output a")
    related_links = []
    for link in links:
        href = link.get_attribute("href")
        if href and "wiki" in href and href not in related_links:
            related_links.append(href)
            if len(related_links) >= 10:
                break
    return related_links


def print_related_links(driver):
    related_links = get_related_links(driver)
    for i, link in enumerate(related_links):
        print(f"{i + 1}. {link}")
    return related_links


def main():
    driver = initialize_driver()
    visited_links = []

    try:
        while True:
            query = input("Введите запрос для поиска на Википедии: ").strip()
            if not query:
                print("Пожалуйста, введите запрос.")
                continue

            search_wikipedia(driver, query)
            visited_links.append(driver.current_url)

            while True:
                print("Выберите действие:")
                print("1. Листать параграфы текущей статьи")
                print("2. Просмотреть список связанных страниц")
                print("3. Ввести новый запрос")
                print("4. Выйти из программы")

                choice = input("Ваш выбор (1, 2, 3, 4): ").strip()

                if choice == '1':
                    print_paragraphs(driver)
                elif choice == '2':
                    related_links = print_related_links(driver)
                    link_choice = input("Введите номер страницы для перехода или 'esc' для выхода: ").strip().lower()
                    if link_choice == 'esc':
                        continue
                    elif link_choice.isdigit() and 1 <= int(link_choice) <= len(related_links):
                        driver.get(related_links[int(link_choice) - 1])
                        visited_links.append(driver.current_url)
                    else:
                        print("Неверный выбор. Попробуйте снова.")
                elif choice == '3':
                    break  # Возвращаемся для ввода нового запроса
                elif choice == '4':
                    print("Выход из программы.")
                    print("Посещенные ссылки:")
                    for link in visited_links:
                        print(link)
                    return
                else:
                    print("Неверный выбор. Попробуйте снова.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()


