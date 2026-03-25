import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        # ✅ First check if the response is OK
        if response.status_code == 200:
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"]
            }

        # ✅ Check for rate limiting
        elif response.status_code == 429:
            return {"error": "Rate limit exceeded. Please try again later."}

        # ✅ Handle other errors
        else:
            return {"error": f"API request failed with status code {response.status_code}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}