import requests
from pprint import pprint

root_api = "http://stapi.co/api/v1/rest/"

entities = [
    'company', 
    'comicStrip', 
    'organization', 
    'soundtrack', 
    'character', 
    'common', 
    'literature', 
    'magazine', 
    'videoRelease', 
    'animal', 
    'comicCollection', 
    'staff', 
    'common', 
    'title',
    'astronomicalObject', 
    'element', 
    'common', 
    'tradingCard', 
    'comics', 
    'tradingCardDeck', 
    'magazineSeries', 
    'videoGame', 
    'technology', 
    'comicSeries', 
    'movie', 
    'performer', 
    'weapon', 
    'episode', 
    'season', 
    'bookSeries', 
    'conflict', 
    'location', 
    'spacecraftClass', 
    'material', 
    'species', 
    'occupation', 
    'bookCollection', 
    'medicalCondition', 
    'food', 
    'tradingCardSet', 
    'oauth', 
    'book', 
    'spacecraft', 
    'series'
]

def form_request(url=root_api, entity='character', type='get', search=True):
    if search == True:
        return requests.type(f"{root_api}{entity}/search")
    else:
        return requests.type(f"{root_api}{entity}")

if __name__ == "__main__":
    pass

form_request(root_api, 'post')