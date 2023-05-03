import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 38.907192
MY_LONG = -77.036873
ISS_API = "http://api.open-notify.org/iss-now.json"
SUNSET_API = "https://api.sunrise-sunset.org/json"
EMAIL = "REDACTED"
PASSWORD = "REDACTED"
MESSAGE = "Subject: ISS\n\nThe International Space Station (ISS) should be visible near you."


def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url=SUNSET_API, params=parameters)
    response.raise_for_status()
    data = response.json()
    time_sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    time_sunrise_min = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
    time_sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_sunset_min = int(data["results"]["sunset"].split("T")[1].split(":")[1])
    time_now = datetime.now()
    if (time_now.hour >= time_sunset_hour and time_now.minute >= time_sunset_min) and \
            (time_now.hour <= time_sunrise_hour and time_now.minute <= time_sunrise_min):
        return True
    return False


def is_iss_above():
    response = requests.get(url=ISS_API)
    response.raise_for_status()
    data = response.json()
    curr_lat = float(data["iss_position"]["latitude"])
    curr_long = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5 <= curr_lat <= MY_LAT + 5) and (MY_LONG - 5 <= curr_long <= MY_LONG + 5):
        return True
    return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=MESSAGE)


while True:
    if is_night() and is_iss_above():
        send_email()
    time.sleep(60)
