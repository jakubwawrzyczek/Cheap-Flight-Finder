import flight_search
from data_manager import DataManager
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = DataManager().get_destination_data()

need_to_update = False

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

# for row in sheet_data:
#     if row['iataCode'] == '':
#         need_to_update = True
#
# if need_to_update:
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row['iataCode'] = flight_search.get_destination_code(row['city'])
#
#     data_manager.destination_data = sheet_data
#     data_manager.put_destination_data()

print(flight_search.FlightSearch().search_for_flight('London', tomorrow, six_months_from_today))