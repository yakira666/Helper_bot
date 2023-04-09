import os
import time
import requests

from dotenv import load_dotenv

load_dotenv("../.env")
BOT_TOKEN: str = os.environ.get("API_TOKEN")
API_URL: str = 'https://api.telegram.org/bot'
offset = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')

