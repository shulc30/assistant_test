import os
import pandas as pd
import requests
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

# Создаем папку 'finel', если она не существует
output_dir = 'finel'
os.makedirs(output_dir, exist_ok=True)

# Читаем слоганы из CSV файла
slogans_file = 'generated_slogans.csv'

if not os.path.exists(slogans_file):
    raise FileNotFoundError(f"Файл {slogans_file} не найден!")

slogans = pd.read_csv(slogans_file)

if slogans.shape[1] < 2:
    raise ValueError("Файл должен содержать как минимум два столбца!")

# Генерируем изображения для первых двух слоганов
for index in range(min(2, len(slogans))):  # ограничиваем до 2 слоганов
    prompt = slogans.iloc[index, 1]  # выбираем второй столбец

    try:
        # Генерация изображения
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )

        # Проверяем, есть ли данные в ответе
        if not response.data:
            print(f"Ошибка: не удалось получить изображение для слогана {index + 1}")
            continue

        image_url = response.data[0].url  # получаем URL изображения

        # Скачивание изображения
        image_response = requests.get(image_url)

        if image_response.status_code != 200:
            print(f"Ошибка при загрузке изображения {index + 1}: {image_response.status_code}")
            continue

        # Путь для сохранения
        file_name = os.path.join(output_dir, f'image_{index + 1}.png')

        # Сохраняем изображение
        with open(file_name, 'wb') as f:
            f.write(image_response.content)

        print(f"Изображение сохранено как {file_name}")

    except Exception as e:
        print(f"Ошибка при генерации изображения {index + 1}: {e}")

print("Процесс завершен.")
