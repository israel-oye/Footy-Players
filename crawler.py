import json
import os

import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()

service_path = os.getenv("CHROME_DRIVER_PATH")
BASE_URL = os.getenv("BASE_URL")

service = Service(service_path)
driver = webdriver.Chrome(service=service)
PLAYERS_API_ENDPOINT = f"{BASE_URL}/483e026bce6c25d2041d"
UPDATE_ENDPOINT = f"{BASE_URL}/ab0d985e937ec02b5021"

resp = requests.get(PLAYERS_API_ENDPOINT, headers={"Content-Type": "application/json"}).json()

updated_players = []

for player in resp["players"]:
    query = player["name"]
    url = "https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
    driver.get(url=url)


    image = driver.find_element(by=By.CSS_SELECTOR, value=".rg_i.Q4LuWd")
    image_url = image.get_attribute("src")

    updated_players.append(
        {
            "id": player['id'],
            "name": player['name'],
            "image": image_url
        }
    )
    print(f"Gotten image url for Player {player['id']}...")


updated_players_json = json.dumps({"players": updated_players})

update_response = requests.post(url=UPDATE_ENDPOINT, data=updated_players_json)
if update_response.status_code == 200:
    print("\nSuccess running script.")


