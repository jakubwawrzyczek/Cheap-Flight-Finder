import flight_search
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = DataManager().get_destination_data()

need_to_update = False

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for row in sheet_data:
    if row['iataCode'] == '':
        need_to_update = True

if need_to_update:
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])

    data_manager.destination_data = sheet_data
    data_manager.put_destination_data()


for row in sheet_data:
    flight = flight_search.FlightSearch().search_for_flight(f'{row["city"]}', tomorrow, six_months_from_today)
    message = f'Low price alert! {flight.price} for flight from ' \
              f'{flight.city_from}({flight.city_from_IATA}) to ' \
              f'{flight.city_to}({flight.city_to_IATA})! \n' \
              f'{flight.out_date} - {flight.return_date}.'

    print(message)
    if flight.price < row['lowestPrice']:
        NotificationManager().send_sms(message)
