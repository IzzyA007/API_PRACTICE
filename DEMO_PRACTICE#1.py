from tkinter import*

root = Tk()
root.title("Izzy Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter your name")

def button_click(number):
    e.delete(0, END)
    e.insert(0, number)

# Defined the buttons to use

button_1 = Button(root, text="1", padx=80, pady=20, command=lambda :button_click(1) ) #To run the number for each function we need a lambada
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda :button_click(2) )
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda :button_click(3) )
button_4 = Button(root, text="4", padx=80, pady=20, command=lambda :button_click(4) )
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda :button_click(5) )
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda :button_click(6) )
button_7 = Button(root, text="7", padx=80, pady=20, command=lambda :button_click(7) )
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda :button_click(8) )
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda :button_click(9) )
button_0 = Button(root, text="0", padx=80, pady=20, command=lambda :button_click(0) )
enter_button = Button(root, text="=", padx=80,pady=30,command=lambda :button_click())
add_button = Button(root, text="+", padx=40,pady=20,command=lambda :button_click())
subtract_button = Button(root, text="-", padx=40,pady=20,command=lambda :button_click())
divide_button = Button(root, text="/", padx=40,pady=20,command=lambda :button_click())
clear_button = Button(root, text="C", padx=80,pady=30,command=lambda :button_click())


#Put the buttons on the screen

#Row 3
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
#Row 2
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
#Row 1
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
enter_button.grid(row=5, column=0)
add_button.grid(row=4, column=1)
subtract_button.grid(row=4, column=2)
divide_button.grid(row=5, column=2)
clear_button.grid(row=5, column=1)






root.mainloop() #This runs the application and keeps it going