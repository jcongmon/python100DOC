from bs4 import BeautifulSoup
import requests
import smtplib
import os

URL = "https://www.amazon.com/dp/B084D1H1MB/ref=twister_B0C3MQYQG7?_encoding=UTF8&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
content = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(content.text, "html.parser")
price = float(soup.select(selector="div > span > span.a-offscreen")[0].getText()[1:])

user = os.environ.get("USER")
item_name = soup.select(selector="div > h1 > span#productTitle")[0].getText().strip()
msg = f"Subject: Amazon Price Alert!\n\n{item_name} is now ${price}!\n{URL}"

if price <= 275.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=os.environ.get("PASSWORD"))
        connection.sendmail(from_addr=user, to_addrs=user, msg=msg)