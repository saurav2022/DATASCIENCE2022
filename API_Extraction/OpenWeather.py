import requests 
import datetime 
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lat": 22.572645,
    "lon": 88.363892,
    "appid" : '...'
}

try:
    response = requests.get(OWM_endpoint, weather_params).json()
    temp = response['main']['temp'] - 273
    feels_like = response['main']['feels_like'] - 273
    print(f"Its {temp} deg C in Kolkata but feels like {feels_like}")

    sunrise = datetime.datetime.fromtimestamp(response['sys']['sunrise'])
    sunset = datetime.datetime.fromtimestamp(response['sys']['sunset']) 
    print(sunrise, sunset, response['sys']['country'])

except:
    pass