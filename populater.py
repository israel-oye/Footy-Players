import datetime
import os

import requests
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")
API_ENDPOINT = "https://api.npoint.io/ab0d985e937ec02b5021"

def get_players():
    resp = requests.get(API_ENDPOINT).json()
    players_list = [player_obj for player_obj in resp['players']]

    return players_list


client = MongoClient(CONNECTION_STRING)
db = client["players_mint"]
players_collection = db["players"]

list_of_players = get_players()
result = players_collection.insert_many(list_of_players)

if players_collection.count_documents({}) == 77:
    print("All done!")
