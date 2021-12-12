import requests

API_KEY = "c3406cdf43ac617ac7ac96eaaa5bae3e"
city = input("Hallo! Bitte gib eine Stadt ein: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metricB&appid={API_KEY}'
print(url)
data = requests.get(url).json()
print(data)
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f'In {city} beträgt die Temperatur {temp}. Die Luftfeuchtigkeit beträgt {humidity}%.')
