# VK Education Projects Bot

Этот проект — чат-бот для ВКонтакте, который отвечает на вопросы о программе VK Education Projects.  
Бот использует API ВКонтакте и Яндекс GPT для генерации ответов на нестандартные вопросы.

---

## Основные возможности

- Отвечает на часто задаваемые вопросы с помощью клавиатуры.
- Генерирует ответы на нестандартные вопросы через Яндекс GPT с контекстом из файла.
- Автоматически обновляет IAM токен для работы с API Яндекс.

---

## Структура проекта

- `config.py` — хранит токены и идентификаторы.
- `iam_token_updater.py` — обновляет IAM токен Яндекс.
- `yandex_gpt.py` — модуль для работы с API Яндекс GPT.
- `main.py` — основной скрипт бота.
- Папка `keyboards/` — JSON-файлы с клавиатурами (`main.json`, `faq.json`, `empty_keyboard.json`).
- Файл `vkeducation.txt` — информация для ответов.

---

## Установка и запуск

1. Склонируйте репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd <папка_проекта>

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt

3. Активируйте виртуальное окружение:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate       # Windows
   # или source .venv/bin/activate (на Mac/Linux)

3. В файл config.py вставьте Ваши токены:
   token = '<VK_API_ТОКЕН>'
   OAUTH_TOKEN = '<YANDEX_OAUTH_TOKEN>'
   FOLDER_ID = '<YANDEX_FOLDER_ID>'
   IAM_TOKEN = None # Не меняется вручную — обновляется автоматически

