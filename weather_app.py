import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("API key not found.")
    exit()

city = input("Enter city name: ")

# Current Weather
weather_url = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

# Forecast
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

forecast_params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    weather_response = requests.get(
        weather_url, params=weather_params, timeout=10
    )

    if weather_response.status_code == 200:
        weather = weather_response.json()

        print("\n===== WEATHER REPORT =====")
        print("City:", weather["name"])
        print("Temperature:", weather["main"]["temp"], "°C")
        print("Humidity:", weather["main"]["humidity"], "%")
        print("Condition:", weather["weather"][0]["description"])

        forecast_response = requests.get(
            forecast_url, params=forecast_params, timeout=10
        )

        if forecast_response.status_code == 200:
            forecast = forecast_response.json()

            print("\n===== FORECAST =====")

            for item in forecast["list"][:5]:
                date_time = item["dt_txt"]
                temperature = item["main"]["temp"]
                condition = item["weather"][0]["description"]

                print(
                    date_time,
                    "|",
                    temperature,
                    "°C |",
                    condition
                )
        else:
            print("\nForecast could not be fetched.")

    elif weather_response.status_code == 401:
        print("Invalid or inactive API key.")

    elif weather_response.status_code == 404:
        print("City not found.")

    else:
        print("Unable to fetch weather data.")
        print("Status code:", weather_response.status_code)

except requests.RequestException as e:
    print("Network error:", e)