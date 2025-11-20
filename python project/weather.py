import requests

API_KEY = "YOUR_API_KEY"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url).json()

print("City:", response["name"])
print("Temperature:", response["main"]["temp"], "°C")
print("Weather:", response["weather"][0]["description"])
