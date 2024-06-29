import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io

# Your API key
api_key = '30d4741c779ba94c470ca1f63045390a'


# Function to get weather data
def get_weather():
    city = city_entry.get()
    if city:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

        if weather_data.json()['cod'] == '404':
            messagebox.showerror("Error", "No City Found")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            result_label.config(text=f"The weather in {city} is: {weather}\nThe temperature in {city} is: {temp}ºF")

            # Get weather icon
            icon_id = weather_data.json()['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)

            # Display weather icon
            weather_icon_label.config(image=icon_photo)
            weather_icon_label.image = icon_photo
    else:
        messagebox.showwarning("Input Required", "Please enter a city name")


# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
city_label = tk.Label(root, text="Enter city:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Create label to display weather icon
weather_icon_label = tk.Label(root)
weather_icon_label.pack(pady=10)

# Run the application
root.mainloop()
