from flight_data import FlightData
import os
from twilio.rest import Client
import requests
import smtplib

AUTHORIZATION = f"Bearer {os.environ.get('TOKEN')}"
SHEETS_USERS_URL = "https://api.sheety.co/a133bcd859feeefcc9df8b9084ffc698/flightDeals/sheet2"


class NotificationManager:
    def __init__(self):
        self.sid = os.environ.get("TWILIO_SID")
        self.token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.sid, self.token)
        self.headers = {"Authorization": AUTHORIZATION}
        self.flight_list = FlightData().flights
        # self.message() FOR TWILIO SMS
        self.send_emails()

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

    def send_emails(self):
        response = requests.get(url=SHEETS_USERS_URL, headers=self.headers)
        response.raise_for_status()
        user_list = response.json()["sheet2"]
        if len(self.flight_list) != 0:
            for user in user_list:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=os.environ.get("EMAIL"), password=os.environ.get("EMAIL_PW"))
                    message = ""
                    for flight in self.flight_list:
                        message += f"Low price alert! Only ${flight['price']} to fly from " \
                                   f"{flight['city_from']}-{flight['fly_from']} to " \
                                   f"{flight['city_to']}-{flight['fly_to']} from " \
                                   f"{flight['departure_date']} to {flight['return_date']}\n. " \
                                   f"Click here: {flight['link']}\n"

                    connection.sendmail(
                        from_addr=os.environ.get("EMAIL"),
                        to_addrs=user["email"],
                        msg=f"Subject: Cheap Flights\n\n"
                            f"Hello {user['firstName']} {user['lastName']},\n {message}"
                    )