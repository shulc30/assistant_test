import os
import requests
import csv
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем API-ключ
API_KEY = os.getenv('NEWS_API_KEY')

if not API_KEY:
    raise ValueError("API-ключ не найден. Убедитесь, что в файле .env указана переменная NEWS_API_KEY")

# URL для получения новостей
url = 'https://newsapi.org/v2/everything'

# Ключевые слова для поиска
keywords = [
    'раннее обучение арифметике',
    'скорочтение',
    'развитие детей',
    'воспитание детей'
]

# Список для хранения статей
articles = []

# Выполнение запросов по каждому ключевому слову
for keyword in keywords:
    params = {
        'q': keyword,
        'apiKey': API_KEY,
        'language': 'ru',
        'sortBy': 'publishedAt',
        'pageSize': 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles.extend(data.get('articles', []))
    else:
        print(f"Ошибка при запросе по ключевому слову '{keyword}': {response.status_code}, Текст ошибки: {response.text}")

# Сохранение статей в CSV-файл
with open('news_articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Заголовок', 'Описание', 'Ссылка', 'Дата публикации'])

    if articles:
        for article in articles:
            writer.writerow([
                article.get('title'),
                article.get('description'),
                article.get('url'),
                article.get('publishedAt')
            ])
        print(f"Найденные статьи сохранены в 'news_articles.csv'.")
    else:
        print("Не найдено статей по вашим запросам.")








