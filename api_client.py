import requests
from typing import Dict

API_KEY = 'b3a444c84bb110dbcfada5928562a9bd'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

class WeatherAPIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather_data(self, city: str) -> Dict:
        params = {
            'q': city,
            'appid': self.api_key
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data for {city}: {response.status_code}")

# Usage
client = WeatherAPIClient(API_KEY)
weather_data = client.get_weather_data("Delhi")
print(weather_data)
