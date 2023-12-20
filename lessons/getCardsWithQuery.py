import requests

search_query = "t:Goblin"
url = f"https://api.scryfall.com/cards/search?q={search_query}"

response = requests.get(url)

if response.status_code == 200:
    search_results = response.json()
    for card in search_results['data']:
        print("Card Name:", card['name'])
        print("Set:", card['set_name'])
        print("Type:", card['type_line'])
        print("---")
else:
    print("Error:", response.status_code)