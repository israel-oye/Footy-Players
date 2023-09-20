import time
import requests
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(r"C:\Users\OLUWAPELUMI\Documents\Python codes\Footy Pic\chromedriver.exe")
driver = webdriver.Chrome(service=service)
PLAYERS_API_ENDPOINT = "https://api.npoint.io/483e026bce6c25d2041d"
UPDATE_ENDPOINT = "https://api.npoint.io/ab0d985e937ec02b5021"

resp = requests.get(PLAYERS_API_ENDPOINT, headers={"Content-Type": "application/json"}).json()

updated_players = []

for player in resp["players"]:
    query = player["name"]
    url = "https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
    driver.get(url=url)

    # time.sleep(2)

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

resp2 = requests.post(url=UPDATE_ENDPOINT, data=updated_players_json)
if resp2.status_code == 200:
    print("\nSuccess running script.")


