import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("API key not found.")
    print("Please set OPENWEATHER_API_KEY first.")
    exit()

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("\n===== Weather Report =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])

    elif response.status_code == 401:
        print("Invalid or inactive API key.")

    elif response.status_code == 404:
        print("City not found.")

    else:
        print("Unable to fetch weather data.")
        print("Status code:", response.status_code)

except requests.RequestException as e:
    print("Network error:", e)