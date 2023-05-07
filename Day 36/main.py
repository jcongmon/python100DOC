import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

AV_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": os.environ.get("AV_KEY"),
}

response = requests.get(url=AV_URL, params=AV_PARAMS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

previous_day_close = None
day_before_yesterday_close = None
previous_day_date = None

for key in data:
    if previous_day_close is None:
        previous_day_close = data[key]["4. close"]
        previous_day_date = key
    elif day_before_yesterday_close is None:
        day_before_yesterday_close = data[key]["4. close"]

percent_change = (float(previous_day_close) - float(day_before_yesterday_close)) / \
                 float(day_before_yesterday_close) * 100

if percent_change > 5 or percent_change < -5:
    NEWS_PARAMS = {
        "apikey": os.environ.get("NEWS_KEY"),
        "q": COMPANY_NAME,
        "from": previous_day_date,
        "language": "en",
        "sortBy": "popularity",
    }

    news_response = requests.get(url=NEWS_URL, params=NEWS_PARAMS)
    news_response.raise_for_status()
    news_data = news_response.json()
    article_titles = [key["title"] for key in news_data["articles"]]
    article_descriptions = [key["description"] for key in news_data["articles"]]

    account_sid = "ACfdfca409c3eb050ada74d66c788db317"
    auth_token = os.environ.get("TWILIO_KEY")
    client = Client(account_sid, auth_token)

    is_up = "🔺" if percent_change > 5 else "🔻"
    for i in range(3):
        message = client.messages.create(
            body=f"{STOCK}: {is_up} {round(percent_change, 2)}% Headline: {article_titles[i]} "
                 f"Brief: {article_descriptions[i]}",
            from_="+18883014664",
            to="+13017682380"
        )
        print(message.status)
