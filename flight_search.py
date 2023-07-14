import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

TEQUILA_API_KEY = f'{os.environ.get("TEQUILA_API_ENV")}'
TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'

HEADERS = {
    'apikey': TEQUILA_API_KEY,
}


class FlightSearch:

    def get_destination_code(self, city_name):
        query = {
            'term': f'{city_name}',
            'location_types': 'city',
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}/locations/query', params=query, headers=HEADERS)
        code = response.json()['locations'][0]['code']
        return code

    def search_for_flight(self, destination, from_time, to_time):
        query = {
            'fly_from': 'WAW',
            'fly_to': f'{self.get_destination_code(destination)}',
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            "flight_type": "round",
            'max_stopovers': 0,
            "one_for_city": 1,
            'curr': 'GBP'
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', params=query, headers=HEADERS)
        return response.json()['data'][0]
