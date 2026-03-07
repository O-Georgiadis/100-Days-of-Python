import requests
from bs4 import BeautifulSoup
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(override=True)
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
cache_path=Path(__file__).parent/".cache"

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = f"https://www.billboard.com/charts/hot-100/{year}"

web_page = requests.get(URL, headers=header)

soup = BeautifulSoup(web_page.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path=cache_path,
        username="Odysseas Georgiadis"

    )
)
user_id = sp.current_user()["id"]