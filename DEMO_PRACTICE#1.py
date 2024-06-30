from tkinter import*

root = Tk()

myButton = Button(root, text= "Click Me!", state=DISABLED, padx=500)
#When you put disabled this would disable the button
# padx is like the padding of the botton x is left and right and y is up and down

myButton.pack() #This just packs it into the window


root.mainloop() #This runs the application and keeps it going
