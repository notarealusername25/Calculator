from tkinter import * # imports everything from tkinter

root = Tk() #root is the window into which all other widgets go
root.title("(Insert name)'s Calcualtor") #sets name of the window

operation_number = 0
current_number_sum = 0
current_number_minus = 0
current_number_division = 0
current_number_multiply = 0

#"Columnspan" tells the layout manager that you wish for this widget to occupy more than 1 column i.e. spans ocross 2 columns
e = Entry(root, width = 50, borderwidth = 5) #"Width" sets the width of the window and "borderwidth" the width of the output box
#"Entry" creates the box where the numbers are printed
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10) #presets both the row and column to 0 so they can be iterated over and changed later, however it enables the same starting position

#both "e" and "e.grid" are used to flesh out the input bok in the calculator
"""def button_click(number, entry): #deals with the output section where resuts get printed
    current_number = e.get()#Returns text
    e.delete(0, END) #deletes text from first and last
    e.insert(0, str(current_number) + str(number))"""
print(dir(Entry))

def button_click(number):
    #e.delete(0, END) #deletes whats currently in the box
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) #inserts number into the textbox

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "power":
        e.insert(0, f_num ** int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_decimal():
    current = e.get()
    if "." in current:
        print("Decimal is in number")
    else:
        e.delete(0, END)
        e.insert(0, (current) + str("."))

"""
def add_point():
    current_number = e.get()
    if "." in current_number:
        print("Number already has a point")
        pass
    else:
        if current_number != "":
            current_number = str(current_number) + str(".")
            e.delete(0,END)
            e.insert(0, current_number)
        else:
            current_number = "0."
            e.insert(0, current_number)"""

def button_delete():
    e.delete([-1])

def button_power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = int(first_number)
    e.delete(0, END)

def button_addminus():
    current = e.get()
    e.delete(0, END)
    if "." in current:
        e.insert(0, -(float(current)))
    else:
        e.insert(0, -(int(current)))

#define code
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1)) #command links to a function which describes what the button can do
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_add = Button(root, text = "+", padx = 40, pady = 20, command = button_add)
button_equal  = Button(root, text = "=", padx = 40, pady = 20, command = button_equal)
button_clear = Button(root, text = "CE", padx = 36, pady = 20, command = button_clear)

button_subtract = Button(root, text = "-", padx = 40, pady = 20, command = button_subtract)
button_multiply = Button(root, text = "×", padx = 39, pady = 20, command = button_multiply)
button_divide = Button(root, text = "÷", padx = 39, pady = 20, command = button_divide)

button_decimal = Button(root, text = ".", padx = 41, pady = 20, command = button_decimal)
button_delete = Button(root, text = "DEL", padx = 33, pady = 20, command = button_delete)
button_power = Button(root, text = "ab", padx = 37, pady = 20, command = button_power)
button_addminus = Button(root, text = "+/-", padx = 34, pady = 20, command = button_addminus)

#Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0, columnspan = 1)
button_add.grid(row=3, column=3)
button_equal.grid(row=5, column=3, columnspan = 1)

button_subtract.grid(row=2, column=3)
button_multiply.grid(row=1, column=3)
button_divide.grid(row=4, column=3)

button_decimal.grid(row=5, column=1)
button_delete.grid(row=5, column=0)
button_power.grid(row=5, column=2)
button_addminus.grid(row=4, column=2)


root.mainloop()
