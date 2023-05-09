import requests
import os

AUTHORIZATION = f"Bearer {os.environ.get('TOKEN')}"
SHEETS_URL = "https://api.sheety.co/a133bcd859feeefcc9df8b9084ffc698/flightDeals/sheet1"


class DataManager:
    def __init__(self):
        self.headers = {"Authorization": AUTHORIZATION}
        self.locations = self.make_dictionary()

    def make_dictionary(self):
        response = requests.get(url=SHEETS_URL, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return {key["iataCode"]: key["lowestPrice"] for key in data["sheet1"]}
