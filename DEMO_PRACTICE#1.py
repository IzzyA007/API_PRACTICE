from tkinter import*

root = Tk()
# Creating a Lebel Widget
myLabel1 = Label(root, text= "My name is Izzy").grid(row=0, column=0)
myLabel2 = Label(root, text= "I like Ferrari").grid(row=1, column=0)
myLabel3 = Label(root, text= " NBA")

# Shoving it onto the screen
# myLabel1.grid(row=1, column=5)
# myLabel2.grid(row=1, column=5)
# myLabel3.grid(row=1, column=5)

root.mainloop() #This runs the application and keeps it going
