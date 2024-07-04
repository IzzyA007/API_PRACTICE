from tkinter import*

root = Tk()
root.title("Izzy Calculator")

e = Entry(root, width=90, borderwidth=5)
e.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter your name")

def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addtion"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiplication():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_Divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get() # This is going to pull whatever is in that textbox
    e.delete(0, END)
    if math == "addtion":
        e.insert(0,f_num + int(second_number))

    if math == "subtraction":
        e.insert(0,f_num - int(second_number))

    if math == "multiplication":
        e.insert(0,f_num * int(second_number))

    if math == "division":
        e.insert(0,f_num / int(second_number))






# Defined the buttons to use

button_1 = Button(root, text="1", padx=80, pady=30, command=lambda :button_click(1) ) #To run the number for each function we need a lambada
button_2 = Button(root, text="2", padx=80, pady=30, command=lambda :button_click(2) )
button_3 = Button(root, text="3", padx=80, pady=30, command=lambda :button_click(3) )
button_4 = Button(root, text="4", padx=80, pady=30, command=lambda :button_click(4) )
button_5 = Button(root, text="5", padx=80, pady=30, command=lambda :button_click(5) )
button_6 = Button(root, text="6", padx=80, pady=30, command=lambda :button_click(6) )
button_7 = Button(root, text="7", padx=80, pady=30, command=lambda :button_click(7) )
button_8 = Button(root, text="8", padx=80, pady=30, command=lambda :button_click(8) )
button_9 = Button(root, text="9", padx=80, pady=30, command=lambda :button_click(9) )
button_0 = Button(root, text="0", padx=80, pady=30, command=lambda :button_click(0) )
enter_button = Button(root, text="=", padx=80,pady=30,command=button_equal)
add_button = Button(root, text="+", padx=80,pady=30,command=button_add)
subtract_button = Button(root, text="-", padx=80,pady=30,command=button_subtraction)
divide_button = Button(root, text="/", padx=80,pady=30,command=button_Divide)
clear_button = Button(root, text="C", padx=80,pady=30,command=button_clear)
multiply_button = Button(root,text="*",padx=80,pady=30,command=button_multiplication)

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
multiply_button.grid(row=5, column=2)
divide_button.grid(row=5, column=4)
clear_button.grid(row=5, column=1)






root.mainloop() #This runs the application and keeps it going