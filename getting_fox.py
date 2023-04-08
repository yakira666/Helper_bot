import os
import time
import requests

from dotenv import load_dotenv

load_dotenv(".env")
BOT_TOKEN: str = os.environ.get("API_TOKEN")
API_URL: str = 'https://api.telegram.org/bot'
API_FOX_URL: str = 'https://randomfox.ca/floof/'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str

while counter < 100:
    print("attempt = ", counter)
    updates = requests.get(f"{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}").json()

    if updates["result"]:
        for result in updates["result"]:
            offset = result["update_id"]
            chat_id = result["message"]["from"]["id"]
            cat_response = requests.get(API_FOX_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()["image"]
                requests.get(f"{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}")
            else:
                requests.get(f"{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}")

    time.sleep(1)
    counter += 1
