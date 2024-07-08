from tkinter import*
import requests
import json
from tkinter import messagebox

root = Tk()
root.title("IzzyWeather°F") #The Title of the App
root.geometry("500x500") #This is the size of the App when displayed/specify size of window
api_key = "b9fe8d9245845e3fca97433d994dff40"
#city = input("Enter Your City: ")
#url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
#response = requests.get(url)

def City_input():
    city_name = txt_box.get("1.0","end-1c")


Label_name = Label(root,text="Name of Your City")
Label_name.config(font =("Courier", 14))
txt_box = Entry(root, width=51, borderwidth=2)
button_1 = Button(root, text="Enter")

Label_name.pack()
txt_box.pack()
button_1.pack()
root.mainloop() #This runs the application and keeps it going
