from flight_data import FlightData
import os
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.sid, self.token)
        self.flight_list = FlightData().flights
        self.message()

    def message(self):
        if len(self.flight_list) == 0:
            message = self.client.messages.create(
                body="No flights available today. Check again tomorrow.",
                from_=os.environ.get("FROM_PHONE"),
                to=os.environ.get("TO_PHONE")
            )
            print(message.status)
        else:
            for flight in self.flight_list:
                message = self.client.messages.create(
                    body=f"Low price alert! Only ${flight['price']} to fly from "
                         f"{flight['city_from']}-{flight['fly_from']} to {flight['city_to']}-{flight['fly_to']} "
                         f"from {flight['departure_date']} to {flight['return_date']}.",
                    from_=os.environ.get("FROM_PHONE"),
                    to=os.environ.get("TO_PHONE")
                )
                print(message.status)
