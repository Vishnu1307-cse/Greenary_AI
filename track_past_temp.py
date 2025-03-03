import requests
from datetime import datetime, timedelta
def get_past_summer_temp(lat, lon):
    last_summer_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={last_summer_date}&end_date={last_summer_date}&daily=temperature_2m_max&timezone=auto"
    
    response = requests.get(url)
    data = response.json()
    
    if "daily" in data and "temperature_2m_max" in data["daily"]:
        return data["daily"]["temperature_2m_max"][0]  # Max temp of that day
    return None