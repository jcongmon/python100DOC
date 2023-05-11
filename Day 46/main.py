from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


URL = "https://www.billboard.com/charts/hot-100"

year = input("Enter a date you want to travel to (YYYY-MM-DD): ")

content = requests.get(url=f"{URL}/{year}/")
content_html = content.text
soup = BeautifulSoup(content_html, "html.parser")

all_titles = soup.select(selector="li > h3#title-of-a-story")
all_artists = soup.select(selector="li > span.c-label.a-no-trucate")
title_list = [title.getText().strip() for title in all_titles]
artist_list = [artist.getText().strip() for artist in all_artists]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                               scope="user-library-read playlist-modify-private",
                                               cache_path=".cache",
                                               redirect_uri=os.environ.get("REDIRECT_URI")))
uri_list = []
for title, artist in zip(title_list, artist_list):
    results = sp.search(q=title, type="track", limit=5)
    for result in results["tracks"]["items"]:
        if result["artists"][0]["name"].lower() in artist.lower():
            uri_list.append(result["uri"])
            break

playlist = sp.user_playlist_create(user=os.environ.get("USER_ID"), name=f'{year} Billboard 100', public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
print(f"\nPlaylist created with {len(uri_list)}/100 of the top 100 songs found.")
