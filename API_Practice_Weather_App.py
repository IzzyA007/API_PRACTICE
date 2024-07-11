import requests
import json
api_key = "b9fe8d9245845e3fca97433d994dff40"
city = input("Enter Your City: ")
url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
response = requests.get(url)

if response.json()["cod"] == "404":
    print("City is not found")
else:

    weather_conditions = response.json()["weather"][0]["main"]
    weather_temp = round(response.json()["main"]["temp"])


    report = f"The weather in {city} is {weather_temp}°F and the conditions are {weather_conditions}"
    print(report)





#JSON (JavaScript Object Notation) is the language of APIs. It encodes data structures for easy machine readability.
# APIs primarily pass data back and forth in JSON format.

#However, if we are specifically interested in countries within a certain region, such as Sub-Saharan Africa,
#we need to utilize query parameters to refine our request. Keep in mind that APIs accept different query parameters,
#which is why consulting the API's documentation is essential.