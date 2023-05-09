from flight_search import FlightSearch
from data_manager import DataManager


class FlightData:
    def __init__(self):
        self.locations = DataManager().locations
        self.flights = self.structure_flights()

    def structure_flights(self) -> list:
        flights = self.get_flights_list()
        data_dict = []
        for flight in flights:
            for idx in range(len(flight)):
                data = {
                    "fly_from": flight[idx]["flyFrom"],
                    "city_from": flight[idx]["cityFrom"],
                    "fly_to": flight[idx]["flyTo"],
                    "city_to": flight[idx]["cityTo"],
                    "price": round(flight[idx]["price"]),
                    "departure_date": flight[idx]["route"][0]["local_departure"].split("T")[0],
                    "return_date": flight[idx]["route"][-1]["local_departure"].split("T")[0],
                    "link": flight[idx]["deep_link"]
                }
                data_dict.append(data)
        return data_dict

    def get_flights_list(self) -> list:
        flight_list = []
        for location in self.locations:
            price = self.locations[location]
            search_location = FlightSearch(location, price)
            if len(search_location.flights) != 0:
                flight_list.append(search_location.flights)
        return flight_list
