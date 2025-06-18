import requests

api_Key = "<YOUR_API_KEY>"
city = input("Enter your city: ")

weather_report = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_Key}&q={city}")
data = weather_report.json()

if weather_report.status_code == 200:
    condition = data['current']['condition']['text']
    temperature = data['current']['temp_c']
    print(f"Weather in {city} city: {condition}, {temperature}°C")
else:
    print("Failed to retrieve weather data. Please check the city name or try again later.")
