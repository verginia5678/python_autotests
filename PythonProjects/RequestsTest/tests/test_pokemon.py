import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4a899a187c55a3f4810db5ac3bc7d516'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '19210'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_code():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['name'] == 'Бодик-Бегемотик'