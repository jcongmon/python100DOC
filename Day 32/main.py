import pandas as pd
import datetime as dt
import smtplib
import random

FILE = "birthdays.csv"
LOWER_LIMIT = 1
UPPER_LIMIT = 3
FP = "./letter_templates/"
my_email = "REDACTED"   # email
password = "REDACTED"   # password

df = pd.read_csv(FILE)
now = dt.datetime.now()

for key, value in df.iterrows():
    if value.day == now.day and value.month == now.month:
        with open(file=f"{FP}letter_{random.randint(LOWER_LIMIT, UPPER_LIMIT)}.txt", mode="r") as letter:
            text = letter.readlines()
            message = "".join(text).replace("[NAME]", value[0])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=value.email, msg=message)