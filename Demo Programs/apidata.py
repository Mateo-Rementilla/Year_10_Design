import requests #Requesting for Api data
import json #Changing the format to json



AIWurl = "https://api.themoviedb.org/3/movie/299536?api_key=9c8df55e285a3d66665e0bff56416de3"
AIWmovie = requests.get(AIWurl) #Requesting for API data from the url
AIWdata = json.loads(AIWmovie.text) #Define data as all of API infromation

print(AIWdata)

{'adult': False, 'backdrop_path': '/lmZFxXgJE3vgrciwuDib0N8CfQo.jpg', 'belongs_to_collection': {'id': 86311, 'name': 'The Avengers Collection', 'poster_path': '/tqXiOD5rTyHgabO73Tpw9JDbd88.jpg', 'backdrop_path': '/zuW6fOiusv4X9nnW3paHGfXcSll.jpg'}, 'budget': 300000000, 'genres': [{'id': 12, 'name': 'Adventure'}, {'id': 28, 'name': 'Action'}, {'id': 878, 'name': 'Science Fiction'}], 'homepage': 'https://www.marvel.com/movies/avengers-infinity-war', 'id': 299536, 'imdb_id': 'tt4154756', 'original_language': 'en', 'original_title': 'Avengers: Infinity War', 'overview': 'As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will on all of reality. Everything the Avengers have fought for has led up to this moment - the fate of Earth and existence itself has never been more uncertain.', 'popularity': 429.511, 'poster_path': '/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg', 'production_companies': [{'id': 420, 'logo_path': '/hUzeosd33nzE5MCNsZxCGEKTXaQ.png', 'name': 'Marvel Studios', 'origin_country': 'US'}], 'production_countries': [{'iso_3166_1': 'US', 'name': 'United States of America'}], 'release_date': '2018-04-25', 'revenue': 2046239637, 'runtime': 149, 'spoken_languages': [{'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}, {'english_name': 'Xhosa', 'iso_639_1': 'xh', 'name': ''}], 'status': 'Released', 'tagline': 'An entire universe. Once and for all.', 'title': 'Avengers: Infinity War', 'video': False, 'vote_average': 8.3, 'vote_count': 20786}