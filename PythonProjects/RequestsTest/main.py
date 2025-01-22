import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4a899a187c55a3f4810db5ac3bc7d516'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemons = {
    "name": "Бульбазавр",
    "photo_id": 2
}

body_names = {
    "pokemon_id": "199549",
    "name": "Бульбазавр2",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "199549"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)'''


'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_names)
print(response.text)'''


response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response.text)