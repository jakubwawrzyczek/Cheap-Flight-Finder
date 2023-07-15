import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_GET_ENDPOINT = os.environ.get("SHEETY_ENDPOINT_ENV")
EMAILS_GET_ENDPOINT = os.environ.get("SHEETY_EMAILS_ENV")

HEADERS = {
    'Authorization': f'Bearer {os.environ.get("SHEETY_TOKEN_ENV")}'
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    # getting data from google sheets using Sheety API
    def get_destination_data(self):
        response = requests.get(url=SHEETY_GET_ENDPOINT, headers=HEADERS)
        self.destination_data = response.json()['prices']
        return self.destination_data

    # putting IATA Code to sheet using Sheety API
    def put_destination_data(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f'{SHEETY_GET_ENDPOINT}/{city["id"]}', json=new_data, headers=HEADERS)

    def get_customer_data(self):
        response = requests.get(url=EMAILS_GET_ENDPOINT, headers=HEADERS)
        data = response.json()['users']
        return data
