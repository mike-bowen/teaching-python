import requests
import json

url = "https://api.scryfall.com/cards/random"
response = requests.get(url)

if response.status_code == 200:
    card_data = response.json()
    pretty_json = json.dumps(card_data, indent=2)
    print("Random Card:", pretty_json)
else:
    print("Error:", response.status_code)
