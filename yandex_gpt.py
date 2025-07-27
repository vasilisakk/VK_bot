import requests
import config
from iam_token_updater import update_iam_token

# Функция для отправки запроса к YandexGPT
def ask_yandex_gpt(prompt):
    if config.IAM_TOKEN is None:
        update_iam_token()

    headers = {
        "Authorization": f"Bearer {config.IAM_TOKEN}"
    }

    data = {
        "modelUri": f"gpt://{config.FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": 2000
        },
        "messages": [
            {
                "role": "user",
                "text": prompt
            }
        ]
    }

    response = requests.post(
        "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
        json=data,
        headers=headers
    )

    if response.status_code == 200:
        return response.json()['result']['alternatives'][0]['message']['text']
    elif response.status_code == 401:
        print("IAM токен устарел. Обновляем...")
        update_iam_token()
        return ask_yandex_gpt(prompt)
    else:
        print("Ошибка от YandexGPT:", response.text)
        return "Извините, я пока не могу ответить на этот вопрос."

# Функция для чтения текста из файла и отправки запроса
def generate_answer_from_file(file_path, user_question):
    # Читаем информацию из текстового файла
    with open(file_path, 'r', encoding='utf-8') as file:
        site_content = file.read()

    # Формируем запрос для YandexGPT с учетом контекста с сайта
    prompt = (f"Вот информация с сайта VK Education Projects:\n{site_content}\n\nНа основе этой информации ответь на следующий вопрос от лица представителя компании:\n{user_question}"
              f" если вопрос не связан с сайтом, ответь на него основываясь на источниках из интернета.")

    # Отправляем запрос к YandexGPT и получаем ответ
    return ask_yandex_gpt(prompt)


