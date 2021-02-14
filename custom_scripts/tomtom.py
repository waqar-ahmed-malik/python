import requests
import json
import datetime
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class CustomException(Exception):
    pass


class Tomtom:
    def __init__(self, key: str):
        retry_strategy = Retry(total=3, status_forcelist=[429, 500], backoff_factor=60)
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        self.session = session
        self.key = key

    
    def get_data(self, address: str, country_set: str = 'US', lat: float = 33.765895, lon: float = -84.413062, radius: int = 15000):
        url = 'https://api.tomtom.com/search/2/geocode/{}.json'.format(address)
        params = {
            'countrySet': country_set,
            'lat': lat,
            'lon': lon,
            'key': self.key,
            'radius': radius
        }
        response = self.session.get(url, params=params)
        return response.status_code, response.json()
