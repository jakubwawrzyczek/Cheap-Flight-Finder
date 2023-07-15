class FlightData:

    # just data form for flight data
    def __init__(self, price, city_from, city_from_IATA, city_to, city_to_IATA, out_date, return_date, via_city='',
                 stop_overs=0,):
        self.price = price
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.city_from = city_from
        self.city_from_IATA = city_from_IATA
        self.city_to = city_to
        self.city_to_IATA = city_to_IATA
        self.out_date = out_date
        self.return_date = return_date
