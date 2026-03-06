import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")


all_movies = soup.find_all(name="h3", class_="title")


movie_titles = [movie.getText() for movie in all_movies]

movies = movie_titles[::-1]

with open(Path(__file__).parent/"movie.txt", mode="w") as f:
    for movie in movies:
        f.write(f"{movie}\n")