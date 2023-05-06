import requests
import os
from twilio.rest import Client

OPW = "https://api.openweathermap.org/data/2.5/onecall"
KEY = os.environ.get("OPW_KEY")
LATITUDE = 38.907192
LONGITUDE = -77.036873

account_sid = "ACfdfca409c3eb050ada74d66c788db317"
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": KEY,
    "exclude": "current,minutely,daily,"
}

response = requests.get(url=OPW, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False
for hour in weather_slice:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+18883014664",
        to="+1234567890"
    )
    print(message.status)
