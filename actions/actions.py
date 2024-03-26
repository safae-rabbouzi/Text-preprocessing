from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests


def run(self, dispatcher, tracker, domain):
    api_key = '5202aef7ffed3be42624ca9b7b46f5ae'
    loc = tracker.get_slot('location')
    print("Location extracted:", loc)  # Add this line to check the extracted location
    current = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(loc, api_key)).json()
    print("API Response:", current)  # Add this line to check the API response
    
    if 'weather' in current:
        country = current['sys']['country']
        city = current['name']
        condition = current['weather'][0]['main'    ]
        temperature_c = current['main']['temp']
        humidity = current['main']['humidity']
        wind_mph = current['wind']['speed']
        
        response = f"It is currently {condition} in {city}, {country}. The temperature is {temperature_c} degrees Celsius, the humidity is {humidity}% and the wind speed is {wind_mph} mph."
    else:
        response = "Sorry, I couldn't retrieve the weather information for that location."
    
    dispatcher.utter_message(response)
    return [SlotSet('location', loc)]

