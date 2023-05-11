from bs4 import BeautifulSoup
import requests

content = requests.get(url="https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&count=100")
soup = BeautifulSoup(content.text, "html.parser")

all_movies = soup.select("h3 > a")
movie_list = [movie.getText() for movie in all_movies]

with open(file="movies.txt", mode="a") as file:
    idx = 1
    for movie in movie_list:
        file.write(f"{idx}. {movie}\n")
        idx += 1
