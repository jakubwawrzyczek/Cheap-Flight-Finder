import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

TEQUILA_API_KEY = f'{os.environ.get("TEQUILA_API_ENV")}'
TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'

HEADERS = {
    'apikey': TEQUILA_API_KEY,
}


class FlightSearch:

    # gets City code using Tequilla API
    def get_destination_code(self, city_name):
        query = {
            'term': f'{city_name}',
            'location_types': 'city',
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}/locations/query', params=query, headers=HEADERS)
        code = response.json()['locations'][0]['code']
        return code

    # searches for flight from London to given City
    def search_for_flight(self, destination, from_time, to_time):
        query = {
            'fly_from': 'LON',
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
        try:
            data = response.json()['data'][0]
        except IndexError:
            query['max_stopovers'] = 2
            response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', params=query, headers=HEADERS)
            try:
                data = response.json()['data'][0]
            except IndexError:
                return None
            else:
                flight_data = FlightData(price=data["price"], city_from=data["route"][0]["cityFrom"],
                                         city_from_IATA=data["route"][0]["flyFrom"], city_to=data["route"][1]["cityTo"],
                                         city_to_IATA=data["route"][1]["flyTo"],
                                         out_date=data["route"][0]["local_departure"].split("T")[0],
                                         return_date=data["route"][2]["local_departure"].split("T")[0],
                                         via_city=data["route"][0]["cityTo"], stop_overs=1)
            return flight_data

        else:
            flight_data = FlightData(price=data['price'], city_from=data['route'][0]['cityFrom'],
                                     city_from_IATA=data['route'][0]['flyFrom'], city_to=data['route'][0]['cityTo'],
                                     city_to_IATA=data['route'][0]['flyTo'],
                                     out_date=data['route'][0]['local_departure'].split('T')[0],
                                     return_date=data['route'][1]['local_departure'].split('T')[0])

            return flight_data
