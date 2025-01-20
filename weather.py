import requests
import json
import python_weather
import asyncio
import os

# Your location and city fetching code
send_url = "http://api.ipstack.com/check?access_key=645be217c1ecc610e92fef3314eda3d5"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

#print(latitude)
#print(longitude)
#print(city)

# Asynchronous weather fetching
async def getweather(city: str) -> dict:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(city)
        current_temp = weather.temperature
        current_weather = weather.description
        all_weather = []

        # Collecting weather forecast data
        for daily in weather:
            temp_list = []
            for hourly in daily:
                temp_list.append(f'{hourly!r}'.split())
            all_weather.append(temp_list)

        return {
            'current_temp': current_temp,
            'current_weather': current_weather,
            'all_weather': all_weather
        }

# To hold the weather data globally
weather_data = {}

# Main entry point to run the async task and fetch weather data
def fetch_weather():
    global weather_data
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # Get weather data asynchronously
    weather_data = asyncio.run(getweather(city))

# Call fetch_weather() to populate the weather_data
fetch_weather()

# Accessing weather data
def return_weather():
    return weather_data.get('all_weather', 'No weather data available')
    
def return_temp():
    return weather_data.get('current_temp', 'No temperature data available')
    
def return_current():
    return weather_data.get('current_weather', 'No weather data available')
