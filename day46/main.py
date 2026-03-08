import requests
from bs4 import BeautifulSoup
from pathlib import Path
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(override=True)
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
cache_path=str(Path(__file__).parent/".cache")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = f"https://www.billboard.com/charts/hot-100/{date}"

web_page = requests.get(URL, headers=header)

soup = BeautifulSoup(web_page.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path=cache_path,

    )
)
user_id = sp.current_user()["id"]

playlist_name='Top 100 Songs'
playlist_description= ''
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)


playlist_id = playlist["id"]

for song in song_names:
    search_results = sp.search(q=song, type="track")
    try:
        track_uri = search_results["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id=playlist_id, items=[track_uri])
    except IndexError:
        print(f"{song} not found on Spotify. Skipped.")