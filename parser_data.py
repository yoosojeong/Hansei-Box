import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HanseiBox.settings')

import django
django.setup()

from _movie.models import MovieModel 

def movieDate():
    num = 1
    movie_li = []

    for n in range(2):
        req = requests.get("https://movie.daum.net/premovie/released?opt=reserve&page=" + str(num))
        html = req.text

        soup = BeautifulSoup(html, 'html.parser')

        movies = soup.find_all("a", class_="link_g")[2:]

        [movie_li.append(movie.text) for movie in movies]
            
        num = 2

    return movie_li

if __name__ == '__main__':

    movies = movieDate()
    
    for count in range(len(movies)):
        MovieModel(title=movies[count]).save()
    