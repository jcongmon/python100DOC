import datetime as dt
import os
import requests

MIN_NIGHTS = 4
MAX_NIGHTS = 14
DAYS_IN_ADV = 180
ADULTS = 2
CURRENCY = "USD"
MAX_STOPOVERS = 1
KIWI_URL = "https://api.tequila.kiwi.com/v2/search"


class FlightSearch:
    def __init__(self, fly_to: str, max_price: int):
        self.fly_from = "WAS"
        self.fly_to = fly_to
        self.now = dt.datetime.now()
        self.from_date = self.now.strftime("%d/%m/%Y")
        self.to_date = (self.now + dt.timedelta(days=DAYS_IN_ADV)).strftime("%d/%m/%Y")
        self.max_price = max_price
        self.headers = {
            "apikey": os.environ.get("KIWI_API_KEY"),
            "Content-Type": "application/json",
        }
        self.params = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.from_date,
            "date_to": self.to_date,
            "nights_in_dst_from": MIN_NIGHTS,
            "nights_in_dst_to": MAX_NIGHTS,
            "flight_type": "round",  # will be deprecated
            "adults": ADULTS,
            "adult_hold_bag": "1,1",
            "adult_hand_bag": "1,1",
            "curr": CURRENCY,
            "partner_market": "us",
            "locale": "en",
            "price_to": self.max_price,
            "max_stopovers": MAX_STOPOVERS,
        }
        self.flights = self.get_flights()

    def get_flights(self) -> list:
        response = requests.get(url=KIWI_URL, headers=self.headers, params=self.params)
        response.raise_for_status()
        return response.json()["data"]
