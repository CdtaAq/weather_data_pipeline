import requests
from utils.logger import get_logger

logger = get_logger()

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        logger.info("Weather data fetched successfully.")
        return response.json()
    else:
        logger.error(f"Failed to fetch data: {response.status_code}")
        return None
