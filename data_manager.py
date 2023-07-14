import requests
import os
from dotenv import load_dotenv

load_dotenv()

sheety_get_endpoint = f'{os.environ.get("SHEETY_ENDPOINT_ENV")}'

headers = {
    'Authorization': f'Bearer {os.environ.get("SHEETY_TOKEN_ENV")}'
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_get_endpoint, headers=headers)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def put_destination_data(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f'{sheety_get_endpoint}/{city["id"]}', json=new_data, headers=headers)
            print(response.text)
