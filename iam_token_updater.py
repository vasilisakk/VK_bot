import requests
import time
import config

def update_iam_token():
    url = "https://iam.api.cloud.yandex.net/iam/v1/tokens"
    headers = {"Content-Type": "application/json"}
    data = {
        "yandexPassportOauthToken": config.OAUTH_TOKEN
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        config.IAM_TOKEN = response.json()['iamToken']
        print("IAM токен успешно обновлён.")
    else:
        print("Ошибка при обновлении IAM токена:", response.text)
