import requests
import datetime as dt
import os

headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_KEY"),
    "Content-Type": "application/json",
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": "ran 6.6 miles",
    "gender": "male",
    "weight_kg": 81.28,
    "height_cm": 175.26,
    "age": 33,
}

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_params)
data = response.json()["exercises"][0]
date = dt.datetime.now().strftime(f"%m/%d/%Y")
time = dt.datetime.now().strftime(f"%I:%M %p")
exercise = data["name"].title()
duration = data["duration_min"]
calories = data["nf_calories"]

sheets_parameters = {
    "sheet1": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    },
}

sheets_headers = {
    "Authorization": f"Bearer {os.environ.get('TOKEN')}"
}

sheets_response = requests.post(url=os.environ.get("SHEETS_ENDPOINT"), json=sheets_parameters, headers=sheets_headers)
print(sheets_response.text)

