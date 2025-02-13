# Умный ассистент для генерации контента

## Описание проекта
Этот проект представляет собой умного ассистента, который автоматически выполняет следующие шаги:

1. **Поиск информации в интернете** - `news.py` находит последние новости, связанные с целевой аудиторией (мамами), особенно в области раннего обучения детей арифметике, скорочтению и другим предметам. Новости сохраняются в `news_articles.csv`.
2. **Создание текста для блога** - `news_gen.py` использует ChatGPT для генерации краткого, но содержательного текста для блога на основе найденных новостей. Тексты сохраняются в `generated_blog_texts.csv`.
3. **Создание лозунгов** - `news_gen_slog.py` использует ChatGPT для выделения основной мысли или лозунга из текста блога. Лозунги сохраняются в `generated_slogans.csv`.
4. **Создание изображения** - `news_gen_photo.py` использует DALL·E-3 для генерации изображения на основе подготовленного текста лозунга. Изображения сохраняются в папке `finel/`.
5. **Сохранение результатов** - `move_file.py` выполняет:
   - Перевод `news_articles.csv` в формат `.docx` и сохранение в `finel/`.
   - Перемещение `generated_slogans.csv` в `finel/`.
6. **Запуск всего процесса** - `main.py` последовательно выполняет все файлы с учетом задержек, необходимых для корректного выполнения парсинга, генерации текста и изображений.

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/shulc30/assistant_test.git
   cd assistant_test
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows
   ```
3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```

## Запуск

Запустите проект командой:
```sh
python main.py
```

## Структура проекта
```
├── finel/                      # Папка для финальных результатов
│   ├── *.png / *.jpg           # Сгенерированные изображения
│   ├── *.docx                  # Документ с текстом блога
│   ├── generated_slogans.csv   # Исходный текст для изображений
├── news.py                     # Парсинг новостей
├── news_gen.py                 # Генерация текста блога
├── news_gen_slog.py            # Выделение основного лозунга
├── news_gen_photo.py           # Генерация изображения
├── move_file.py                # Сохранение результатов
├── main.py                     # Основной файл запуска
├── requirements.txt            # Список зависимостей
├── README.md                   # Документация проекта
```

## Используемые технологии
- `requests` - для парсинга новостей.
- `openai` - для генерации текстов и изображений (ChatGPT и DALL·E-3).
- `pandas`, `python-docx` - для обработки и сохранения данных.

## Возможные улучшения
- Добавить возможность выбора источников новостей.
- Улучшить фильтрацию и обработку новостей.
- Добавить более сложную обработку изображений (например, стилизацию или наложение текста).
- Реализовать асинхронное выполнение задач для ускорения работы.

