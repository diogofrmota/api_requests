import requests

url = "http://api.weatherapi.com/v1/current.json?key=494151f4d911472bac9132613263101&q=London&aqi=no"

response = requests.get(url)
weather_data = response.json()

with open('weather.json', 'w') as file:
    import json
    json.dump(weather_data, file, indent=2)

print("File 'weather.json' created with weather data.")
