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

# Инициализация клиента VseGPT
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.vsegpt.ru/v1",
)

def generate_slogan(blog_text):
    prompt = f"Выдели основную мысль или лозунг из следующего текста:\n\n{blog_text}"

    messages = [{"role": "user", "content": prompt}]

    # Отправка запроса на генерацию
    response_big = client.chat.completions.create(
        model="anthropic/claude-3-haiku",
        messages=messages,
        temperature=0.7,
        n=1,
        max_tokens=100,
        extra_headers={"X-Title": "My App"},
    )

    return response_big.choices[0].message.content.strip()

def process_blog_texts(csv_file_path):
    # Чтение CSV-файла
    df = pd.read_csv(csv_file_path)

    # Проверка наличия столбца 'Текст блога'
    if 'Текст блога' not in df.columns:
        raise ValueError("CSV файл должен содержать столбец 'Текст блога'")
    
    slogans = []

    # Обработка текстов блога
    for index, row in df.iterrows():
        blog_text = row['Текст блога']
        slogan = generate_slogan(blog_text)
        slogans.append({'Текст блога': blog_text, 'Лозунг': slogan})
        print(f"Лозунг для блога {index + 1}: {slogan}")

    # Запись результатов в новый CSV-файл
    slogans_df = pd.DataFrame(slogans)
    slogans_df.to_csv('generated_slogans.csv', index=False)
    print("Лозунги сохранены в 'generated_slogans.csv'.")

# Путь к вашему CSV-файлу
csv_file_path = "generated_blog_texts.csv"
process_blog_texts(csv_file_path)
