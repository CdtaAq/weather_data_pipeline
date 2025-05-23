from ingestion.fetch_weather import fetch_weather_data
from transformation.clean_data import transform_weather_data
from storage.save_to_db import save_to_db
from config.settings import API_KEY, CITY

def run_pipeline():
    raw_data = fetch_weather_data(CITY, API_KEY)
    if raw_data:
        clean_data = transform_weather_data(raw_data)
        save_to_db(clean_data)

if __name__ == "__main__":
    run_pipeline()
