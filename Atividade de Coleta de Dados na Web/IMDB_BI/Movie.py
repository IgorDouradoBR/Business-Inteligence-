import requests
import shutil

class Movie():
    def __init__(self, title, poster_url, rate, description, keywords, genres):
        self.title = title
        self.poster_path = self.download_poster(poster_url)
        self.rate = rate
        self.description = description
        self.keywords = keywords
        self.genres = genres
        
    def download_poster(self, poster_url):
        response = requests.get(poster_url, stream=True)
        with open(f'./Posters/{self.title}.png', 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        
        return f'./Posters/{self.title}.png'
        
        