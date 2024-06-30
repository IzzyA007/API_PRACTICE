from tkinter import*

root = Tk()
def myClick():
    myLabel1 = Label(root, text= "My botton works")
    myLabel1.pack()

myButton = Button(root, text= "Click Me!", command=myClick)
# Command= makes the button run a function
# padx is like the padding of the botton x is left and right and y is up and down

myButton.pack() #This just packs it into the window


root.mainloop() #This runs the application and keeps it going
