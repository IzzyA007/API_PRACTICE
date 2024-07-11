import tkinter as tk
from tkinter import messagebox
import requests
import json
from PIL import Image, ImageTk
import io

def City_input():
    city_name = txt_box.get().strip()
    if city_name:
        api_key = "b9fe8d9245845e3fca97433d994dff40"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            display_weather(weather_data)
        else:
            messagebox.showerror("Error", "City not found or API request failed.")
    else:
        messagebox.showerror("Error", "Please enter a city name.")

def display_weather(weather_data):
    main = weather_data['main']
    wind = weather_data['wind']
    weather_desc = weather_data['weather'][0]['description']
    temperature = main['temp']
    feels_like = main['feels_like']
    humidity = main['humidity']
    wind_speed = wind['speed']

    weather_info = (f"Weather: {weather_desc}\n"
                    f"Temperature: {temperature}°F\n"
                    f"Feels Like: {feels_like}°F\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind_speed} mph")

    icon_id = weather_data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    icon_response = requests.get(icon_url)
    icon_image = Image.open(io.BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Display weather icon
    weather_icon_label.config(image=icon_photo)
    weather_icon_label.image = icon_photo

    weather_label.config(text=weather_info)

root = tk.Tk()
root.title("IzzyWeather°F")  # The Title of the App
root.geometry("500x500")  # This is the size of the App when displayed/specify size of window

Label_name = tk.Label(root, text="Name of Your City")  # This is the title for the textbox
Label_name.config(font=("Courier", 14))  # This is the font
txt_box = tk.Entry(root, width=51, borderwidth=2)  # The text box size
button_1 = tk.Button(root, text="Enter", command=City_input)  # This is the button

Label_name.pack()
txt_box.pack()
button_1.pack()

weather_label = tk.Label(root, text="", font=("Courier", 12))
weather_label.pack()

# Create label to display weather icon
weather_icon_label = tk.Label(root)
weather_icon_label.pack(pady=10)

root.mainloop()  # This runs the application and keeps it going
