'''
1) weather check 
2) sunny,rain,heavyrain
3)scale up the pods based on these info
'''
import os 
from dotenv import load_dotenv
import requests
import subprocess


load_dotenv()
api_key = os.getenv("WEA_API_KEY")



def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

print("This is the weather app you can use this app to check the weather of any city")
input_city = input("Enter the city name: ")

weather_data = get_weather(input_city)
weather = weather_data['weather'][0]['main']
print(f"The weather in {input_city} is {weather}")

if weather == 'Rain' or weather == 'Drizzle' or weather == 'Thunderstorm':
    subprocess.run(['kubectl', 'scale', 'deployment', 'pod', '--replicas=5'])

elif weather == 'Clouds':
    subprocess.run(['kubectl', 'scale', 'deployment', 'pod', '--replicas=4'])

else:
    subprocess.run(['kubectl', 'scale', 'deployment', 'pod', '--replicas=2'])
    




