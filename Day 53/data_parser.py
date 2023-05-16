from bs4 import BeautifulSoup
import requests


class DataParser:
    def __init__(self):
        self.url = "https://www.zillow.com/washington-dc/?searchQueryState=%7B%22usersSearchTerm%22%3A%22New%20York" \
                   "%2C%20NY%22%2C%22mapBounds%22%3A%7B%22north%22%3A39.04128435324174%2C%22east%22%3A-76.8326149404" \
                   "2968%2C%22south%22%3A38.74574755409144%2C%22west%22%3A-77.1965370595703%7D%2C%22isMapVisible%22%3" \
                   "Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah" \
                   "%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2494%7D%2C%22price%22%3A%7B%22max%22%3" \
                   "A500000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22doz%22%3" \
                   "A%7B%22value%22%3A%2230%22%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value" \
                   "%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%" \
                   "2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22is" \
                   "ListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A41568%2C%22regionType%22%" \
                   "3A6%7D%5D%2C%22pagination%22%3A%7B%7D%2C%22mapZoom%22%3A11%7D"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        self.response = requests.get(url=self.url, headers=self.headers).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.results = self.soup.select(selector="div#grid-search-results > ul > li")
        self.data_matrix = self.create_ds()

    def create_ds(self) -> list:
        matrix = []
        temp_list = []
        for result in self.results:
            try:
                address = result.find("address").text
                temp_list.append(address)
            except AttributeError:
                continue
        matrix.append(temp_list)
        temp_list = []
        for result in self.results:
            try:
                price = result.find(name="span", attrs={"data-test": "property-card-price"}).text
                temp_list.append(price)
            except AttributeError:
                continue
        matrix.append(temp_list)
        temp_list = []
        for result in self.results:
            try:
                link = result.find(name="a", attrs={"data-test": "property-card-link"}).get("href")
                temp_list.append(link)
            except AttributeError:
                continue
        matrix.append(temp_list)
        return matrix
