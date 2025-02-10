import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем API-ключ
API_KEY = os.getenv('VSEGPT_API_KEY')

if not API_KEY:
    raise ValueError("API-ключ не найден. Убедитесь, что в файле .env указана переменная VSEGPT_API_KEY")

# Инициализация клиента
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.vsegpt.ru/v1",
)

def generate_blog_text(news_title, news_content):
    # Формирование запроса
    prompt = f'''
    Напиши краткий, но содержательный текст для блога, подходящий для мам на основе следующей новости:

    Заголовок: {news_title}
    Описание: {news_content}

    Текст должен быть простым и понятным, с рекомендациями для мам.
    '''
    
    messages = [{"role": "user", "content": prompt}]

    response_big = client.chat.completions.create(
        model="anthropic/claude-3-haiku",
        messages=messages,
        temperature=0.7,
        n=1,
        max_tokens=3000,
        extra_headers={"X-Title": "My App"},
    )

    return response_big.choices[0].message.content  # Получение текста из ответа

# Чтение файла с новостями
news_df = pd.read_csv('news_articles.csv')

# Просмотр имен столбцов для понимания
print(news_df.columns)

# Использование правильных названий столбцов
blog_texts = []

for _, row in news_df.iterrows():
    title = row['Заголовок']
    content = row['Описание']
    
    blog_entry = generate_blog_text(title, content)
    blog_texts.append({'Заголовок': title, 'Текст блога': blog_entry})

# Сохранение текстов блога в новый CSV-файл
blog_df = pd.DataFrame(blog_texts)
blog_df.to_csv('generated_blog_texts.csv', index=False)

print("Тексты для блога успешно сгенерированы и сохранены в 'generated_blog_texts.csv'.")







