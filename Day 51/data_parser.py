from bs4 import BeautifulSoup
import requests
import datetime as dt
import os
AMEX_URL = os.environ.get("AMEX_URL")


def get_curr_idx() -> int:
    with open(file="data.txt", mode="r") as f:
        num = f.readline().strip()
    return int(num)


def set_curr_idx(idx: int):
    with open(file="data.txt", mode="w") as f:
        f.write(str(idx))


def convert_time(string: str) -> str:
    d = dt.datetime.strptime(string, '%B %d')
    return d.strftime(f'{dt.datetime.now().year}-%m-%d')


class DataParser:
    def __init__(self):
        self.curr_idx = get_curr_idx()
        self.current_deals = self.get_deals()

    def get_deals(self) -> dict:
        content = requests.get(url=AMEX_URL).text
        soup = BeautifulSoup(content, "html.parser")
        curr_table = soup.select(selector="div > table > tbody")[0]
        return self.create_curr_dict(curr_table)

    def create_curr_dict(self, table) -> dict:
        data_dict = {}
        for row in table:
            row_list = []
            for tr in row:
                row_list.append(tr.text[:len(tr.text) - 1])
            data_dict[self.curr_idx] = row_list
            self.curr_idx += 1

        for idx, row in data_dict.items():
            data_dict[idx] = {
                "name": data_dict[idx][0],
                "percentage": data_dict[idx][1],
                "conversion": data_dict[idx][2],
                "end_date": convert_time(" ".join(data_dict[idx][3].split(" ")[1:])),
            }

        return data_dict
