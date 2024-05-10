import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём объект переводчика
translator = Translator()


# Функция для получения слова и его определения с переводом
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            english_word = soup.find("div", id="random_word").text.strip()
            word_definition = soup.find("div", id="random_word_definition").text.strip()

            # Переводим слово и определение
            translated_word = translator.translate(english_word, dest='ru').text
            translated_definition = translator.translate(word_definition, dest='ru').text

            return {
                "english_word": english_word,
                "translated_word": translated_word,  # Возвращаем переведённое слово
                "word_definition": translated_definition
            }
        else:
            print("Не удалось получить ответ от сервера")
            return None
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        return None


# Функция, которая проводит игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            print("Попробуем загрузить слово еще раз...")
            continue  # Если произошла ошибка, попробуйте получить слово снова
        translated_word = word_dict.get("translated_word")
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Какое слово вы думаете было загадано? ")

        if user.lower() == translated_word.lower():
            print(f"Все верно: было загадано это слово - {translated_word} ({word})")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word} ({word})")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again.lower() != 'y':
            print("Спасибо за игру!")
            break


word_game()




