from googlesearch import search  # Импорт функции для поиска

def fetch_sites(query, num_results=5):
    # Ищем сайты по заданному запросу
    result_sites = []
    results = search(query, lang="ru", num=num_results, stop=num_results)
    for result in results:
        result_sites.append(f"https://{result.split('/')[2]}/")
    return result_sites

def main():
    # Задаем ключевое слово для поиска
    keyword = "колесо"

    # Получаем список сайтов
    sites = fetch_sites(keyword)

    # Выводим список сайтов
    for site in sites:
        print(site)

if __name__ == "__main__":
    main()
