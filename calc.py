from tkinter import *
import math

root = Tk()
root.title("Ayomide's Scientific Calculator")

operation_number = 0
current_number_sum = 0
current_number_minus = 0
current_number_division = 0
current_number_multiply = 0
current_number_power = 0

e_one = Entry(root, width = 46, borderwidth = 5)
e_one.grid(row = 0, column = 0, columnspan = 5)

e = Entry(root, width = 46, borderwidth = 5)
e.grid(row = 1, column = 0, columnspan = 5)

def button_click(number):
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, str(current_number) + str(number))

def button_add():
    global current_number_sum, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_sum = e.get()
        if current_number_sum != "":
            e.delete(0, END)
            operation_number = 1
        else:
            e.insert(0, "please input a number")
            pass
    elif operation_number == 1:
        new_current_number = e.get()
        e.delete(0, END)
        if "." in str(current_number_sum):
            current_number_sum = float(current_number_sum) + float(new_current_number)
            e.insert(0, current_number_sum)
        else:
            current_number_sum = int(current_number_sum) + int(new_current_number)
            e.insert(0, str(current_number_sum))

def button_subtract():
    global current_number_minus, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_minus = e.get()
        if current_number_minus != "":
            e.delete(0, END)
            operation_number = 2
        else:
            e.insert(0, "please input a number")
            pass
    elif operation_number == 2:
        new_current_number = e.get()
        e.delete(0, END)
        if "." in str(current_number_minus):
            current_number_minus = float(current_number_minus) - float(new_current_number)
            e.insert(0, current_number_minus)
        else:
            current_number_minus = int(current_number_minus) - int(new_current_number)
            e.insert(0, str(current_number_minus))

def button_multiply():
    global current_number_multiply, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_multiply = e.get()
        if current_number_multiply != "":
            e.delete(0, END)
            operation_number = 3
        else:
            e.insert(0, "please input a number")
            pass
    elif operation_number == 3:
        new_current_number = e.get()
        e.delete(0, END)
        if "." in str(current_number_multiply):
            current_number_multiply = float(current_number_multiply) * float(new_current_number)
            e.insert(0, current_number_multiply)
        else:
            current_number_multiply = int(current_number_multiply) * int(new_current_number)
            e.insert(0, str(current_number_multiply))

def button_divide():
    global current_number_division, operation_number
    if operation_number == 0:
        new_current_number = 0
        current_number_division = e.get()
        if current_number_division != "":
            e.delete(0, END)
            operation_number = 4
        else:
            e.inert(0, "please input a number")
            pass
    elif operation_number == 4:
        new_current_number = e.get()
        e.delete(0, END)

        try:
            if "." in str(current_number_division):
                current_number_division = float(current_number_division) / float(new_current_number)
                e.insert(0, current_number_division)
            else:
                current_number_division = int(current_number_division) / int(new_current_number)
                e.insert(0, str(current_number_division))
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

def button_decimal():
    current_number = e.get()
    if "." in current_number:
        e.insert(0, "Number already has a point")
        pass
    else:
        if current_number != "":
            current_number = str(current_number) + str(".")
            e.delete(0, END)
            e.insert(0, current_number)
        else:
            current_number = "0."
            e.insert(0, current_number)

def button_delete():
    try:
        current_number = e.get()
        e.delete(0, END)
        e_one.delete(0, END)
        current_number = current_number[:-1]
        e.insert(0, current_number)
    except:
        e.insert(0, "No number to delete")
        pass

def button_addminus():
    current = e.get()
    e.delete(0, END)
    try:
        if "." in current:
            e.insert(0, - (float(current)))
        else:
            e.insert(0, - (int(current)))
    except ValueError:
        e.insert(0, "please input a number")

def button_clear():
    global operation_number, current_number_sum, current_number_minus, \
        current_number_division, current_number_multiply
    operation_number = 0
    current_number_sum = 0
    current_number_minus = 0
    current_number_division = 0
    current_number_multiply = 0
    e.delete(0, END)
    e_one.delete(0, END)

#Weird extra
def button_pi():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 17
    else:
        e.insert(0, "please input a number")
        pass

def button_e():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 18
    else:
        e.insert(0, "please input a number")
        pass

def button_1overx():
    pass

def button_dashxdash():
    pass

def button_exp():
    pass

def button_mod():
    pass

def button_open():
    pass

def button_close():
    pass

def button_nexc():
    pass

#trig and function
def button_frig():
    pass

def button_func():
    pass


#M buttons
def button_Mc():
    pass

def button_Mr():
    pass

def button_Mplus():
    pass

def button_Mminus():
    pass

def button_MS():
    pass



#top buttons
def button_FE():
    pass

def button_RAD():
    pass

def button_GRAD():
    pass

def button_DEG():
    pass



#2nd button
def button_2():
    pass


#phase1 powers
def button_power2():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 6
    else:
        e.insert(0, "please input a number")
        pass

def button_power3():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 7
    else:
        e.insert(0, "please input a number")
        pass

def button_powery():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 5
    else:
        e.insert(0, "please input a number")
        pass

def button_10powerx():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 8
    else:
        e.insert(0, "please input a number")
        pass

def button_log():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 9
    else:
        e.insert(0, "please input a number")
        pass

def button_ln():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 10
    else:
        e.insert(0, "please input a number")
        pass

#phase2 roots
def button_root2():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 11
    else:
        e.insert(0, "please input a number")
        pass

def button_root3():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 12
    else:
        e.insert(0, "please input a number")
        pass

def button_rooty():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 13
    else:
        e.insert(0, "please input a number")
        pass

def button_twopowerx():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 14
    else:
        e.insert(0, "please input a number")
        pass

def button_logyx():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 15
    else:
        e.insert(0, "please input a number")
        pass

def button_epowerx():
    global current_number_power, operation_number
    current_number_power = e.get()
    if current_number_power != "":
        e.delete(0, END)
        operation_number = 16
    else:
        e.insert(0, "please input a number")
        pass


#blank buttons
def button_one():
    pass

def button_two():
    pass

def button_three():
    pass

def button_four():
    pass

def button_five():
    pass

def button_six():
    pass

def button_seven():
    pass

def button_eight():
    pass

def button_nine():
    pass

def button_ten():
    pass

def button_equal():
    global current_number_sum, current_number_minus, current_number_multiply, operation_number
    current_number = e.get()
    e.delete(0, END)
    if operation_number == 0:
        e.insert(0, current_number)
        e.insert(0, "nothing to do")
    elif operation_number == 1:
        if "." in str(current_number_sum):
            e.insert(0, float(current_number_sum) + float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_sum) + int(current_number))
            operation_number = 0
    elif operation_number == 2:
        if "." in current_number_minus:
            e.insert(0, float(current_number_minus) - float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_minus) - int(current_number))
            operation_number = 0
    elif operation_number == 3:
        if "." in current_number_multiply:
            e.insert(0, float(current_number_multiply) * float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_multiply) * int(current_number))
            operation_number = 0
    elif operation_number == 4:

        try:
            if "." in current_number_division:
                e.insert(0, float(current_number_division) / float(current_number))
                operation_number = 0
            else:
                e.insert(0, int(current_number_division) / int(current_number))
                operation_number = 0
        except ZeroDivisionError:
            e.insert(0, 'Can not divide by zero.')

    elif operation_number == 5:
        if "." in current_number_power:
            e.insert(0, float(current_number_power) ** float(current_number))
            operation_number = 0
        else:
            e.insert(0, int(current_number_power) ** int(current_number))
            operation_number = 0

    elif operation_number == 6:
        if "." in current_number_power:
            e.insert(0, float(current_number_power) ** float(2))
            operation_number = 0
        else:
            e.insert(0, int(current_number_power) ** int(2))
            operation_number = 0

    elif operation_number == 7:
        if "." in current_number_power:
            e.insert(0, float(current_number_power) ** float(3))
            operation_number = 0
        else:
            e.insert(0, int(current_number_power) ** int(3))
            operation_number = 0

    elif operation_number == 8:
        if "." in current_number_power:
            e.insert(0, float(10) ** float(current_number_power))
            operation_number = 0
        else:
            e.insert(0, int(10) ** int(current_number_power))
            operation_number = 0

    elif operation_number == 9:
        if "." in current_number_power:
            e.insert(0, math.log10(float(current_number_power)))
            operation_number = 0
        else:
            e.insert(0, math.log10(int(current_number_power)))
            operation_number = 0

    elif operation_number == 10:
        if "." in current_number_power:
            e.insert(0, math.log(float(current_number_power)))
            operation_number = 0
        else:
            e.insert(0, math.log(int(current_number_power)))
            operation_number = 0

    elif operation_number == 11:
        if "." in current_number_power:
            e.insert(0, math.sqrt(float(current_number_power)))
            operation_number = 0
        else:
            e.insert(0, math.sqrt(int(current_number_power)))
            operation_number = 0

    elif operation_number == 12:
        if "." in current_number_power:
            e.insert(0, float(current_number_power) ** (1/float(3)))
            operation_number = 0
        else:
            e.insert(0, int(current_number_power) ** (1/int(3)))
            operation_number = 0

    elif operation_number == 13:
        if "." in current_number_power:
            e.insert(0, float(current_number) ** (1/(float(current_number_power))))
            operation_number = 0
        else:
            e.insert(0, int(current_number) ** (1/(int(current_number_power))))
            operation_number = 0

    elif operation_number == 14:
        if "." in current_number_power:
            e.insert(0, float(2) ** float(current_number_power))
            operation_number = 0
        else:
            e.insert(0, int(2) ** int(current_number_power))
            operation_number = 0

    elif operation_number == 15:
        if "." in current_number_power:
            e.insert(0, math.log(float(current_number), (float(current_number_power))))
            operation_number = 0
        else:
            e.insert(0, math.log(int(current_number), (int(current_number_power))))
            operation_number = 0

    elif operation_number == 16:
        if "." in current_number_power:
            e.insert(0, math.exp(float(current_number_power)))
            operation_number = 0
        else:
            e.insert(0, math.exp(int(current_number_power)))
            operation_number = 0

    elif operation_number == 17:
        if "." in current_number_power:
            e.insert(0, math.pi * float(current_number_power))
            e_one.insert(0, str(current_number_power) + "π")
            operation_number = 0
        else:
            e.insert(0, math.pi * int(current_number_power))
            e_one.insert(0, str(current_number_power) + "π")
            operation_number = 0

    elif operation_number == 18:
        if "." in current_number_power:
            e.insert(0, math.e * float(current_number_power))
            e_one.insert(0, math.e)
            operation_number = 0
        else:
            e.insert(0, math.e * int(current_number_power))
            e_one.insert(0, math.e)
            operation_number = 0

#Special buttons

class Calc(Frame):
    def __init__(self, master):
        self.modefunction = 1
        super(Calc,self).__init__(master)
        self.grid()
#sets the background of the button to the color specified in the code
#        self.calculations_frm = Frame(self, width=100, height=30, bg = "red")#bg = "red"
#        self.calculations_frm.grid(row = 6, column = 0, columnspan=2)

        self.buttons_frm_1 = Frame(self, width=0, height=0, bg="pink")  # bg = "pink")
        self.buttons_frm_1.grid(row=2, column=0, rowspan=3, columnspan=5)  # hitler

        self.buttons_frm_2 = Frame(self, width=0, height=0, bg="red")  # bg = "red")
        self.buttons_frm_2.grid(row=7, column=1, rowspan=7, columnspan=4)

        self.buttons_frm_3 = Frame(self, width=0, height=0, bg="yellow")  # bg = "red")
        self.buttons_frm_3.grid(row=5, column=0, rowspan=2, columnspan=5)

        self.buttons_frm = Frame(self, width= 0, height=0, bg="green")#bg = "green") #2nd button
        self.buttons_frm.grid(row = 7, column = 0) #hitler


        self.buttons_2_functions_1_frm = Frame(self, width=0, height=0, bg = "blue")#bg = "blue") #Phase 1 and 2
        self.buttons_2_functions_1_frm.grid(row = 8, column = 0, rowspan=6)
        self.create_GUI()
#prints text above the set of buttons
#    def create_show_calculations(self):
#        self.calculation_lbl = Label(self.calculations_frm, text = "will show caluclations here").pack()

#creates unmoveable buttons which are mc and plus both are similar
    def create_buttons(self):
        #mc stands for mode change
        self.button_2 = Button(self.buttons_frm, text = "2nd", command = self.mode_change, padx = 13, pady = 10)
        self.button_2.grid(row = 5,column = 0)

        # Numbers
        self.button_1 = Button(self.buttons_frm_2, text = "1", padx = 20, pady = 10, command = lambda: button_click(1), bg = "grey").grid(row=12, column=1)
        self.button_2 = Button(self.buttons_frm_2, text = "2", padx = 20, pady = 10, command = lambda: button_click(2), bg = "grey").grid(row=12, column=2)
        self.button_3 = Button(self.buttons_frm_2, text = "3", padx = 20, pady = 10, command = lambda: button_click(3), bg = "grey").grid(row=12, column=3)
        self.button_4 = Button(self.buttons_frm_2, text = "4", padx = 20, pady = 10, command = lambda: button_click(4), bg = "grey").grid(row=11, column=1)
        self.button_5 = Button(self.buttons_frm_2, text = "5", padx = 20, pady = 10, command = lambda: button_click(5), bg = "grey").grid(row=11, column=2)
        self.button_6 = Button(self.buttons_frm_2, text = "6", padx = 20, pady = 10, command = lambda: button_click(6), bg = "grey").grid(row=11, column=3)
        self.button_7 = Button(self.buttons_frm_2, text = "7", padx = 20, pady = 10, command = lambda: button_click(7), bg = "grey").grid(row=10, column=1)
        self.button_8 = Button(self.buttons_frm_2, text = "8", padx = 20, pady = 10, command = lambda: button_click(8), bg = "grey").grid(row=10, column=2)
        self.button_9 = Button(self.buttons_frm_2, text = "9", padx = 20, pady = 10, command = lambda: button_click(9), bg = "grey").grid(row=10, column=3)
        self.button_0 = Button(self.buttons_frm_2, text = "0", padx = 20, pady = 10, command = lambda: button_click(0), bg = "grey").grid(row=13, column=2)

        #blank buttons
        self.button_one = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_one).grid(row=5, column=0)
        self.button_two = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_two).grid(row=5, column=1)
        self.button_three = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_three).grid(row=5, column=2)
        self.button_four = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_four).grid(row=5, column=3)
        self.button_five = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_five).grid(row=5, column=4)
        self.button_six = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_six).grid(row=6, column=0)
        self.button_seven = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_seven).grid(row=6, column=1)
        self.button_eight = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_eight).grid(row=6, column=2)
        self.button_nine = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_nine).grid(row=6, column=3)
        self.button_ten = Button(self.buttons_frm_3, text = "", padx = 23, pady = 10, command = button_ten).grid(row=6, column=4)


        #Stndard Math equations
        self.button_subtract = Button(self.buttons_frm_2, text = "-", padx = 21, pady = 10, command = button_subtract).grid(row=11, column=4)
        self.button_multiply = Button(self.buttons_frm_2, text = "×", padx = 19, pady = 10, command = button_multiply).grid(row=10, column=4)
        self.button_divide = Button(self.buttons_frm_2, text = "÷", padx = 19, pady = 10, command = button_divide).grid(row=9, column=4)
        self.button_decimal = Button(self.buttons_frm_2, text = ".", padx = 22, pady = 10, command = button_decimal).grid(row=13, column=3)
        self.button_add = Button(self.buttons_frm_2, text = "+", padx = 19, pady = 10, command = button_add).grid(row=12, column=4)
        self.button_equal = Button(self.buttons_frm_2, text = "=", padx = 19, pady = 10, command = button_equal, bg = "lightblue").grid(row=13, column=4, columnspan = 1)
        self.button_addminus = Button(self.buttons_frm_2, text = "+/-", padx = 14, pady = 10, command = button_addminus).grid(row=13, column=1)

        #Remove Buttons
        self.button_delete = Button(self.buttons_frm_2, text = "DEL", padx = 13, pady = 10, command = button_delete, fg = "white", bg = "orange").grid(row=7, column=4)
        self.button_clear = Button(self.buttons_frm_2, text = "CE", padx = 16, pady = 10, command = button_clear, fg = "white", bg = "orange").grid(row=7, column=3, columnspan = 1)

        #Weird extra
        self.button_pi = Button(self.buttons_frm_2, text = "π", padx = 19, pady = 10, command = button_pi).grid(row=7, column=1)
        self.button_e = Button(self.buttons_frm_2, text = "e", padx = 20, pady = 10, command = button_e).grid(row=7, column=2)
        self.button_1overx = Button(self.buttons_frm_2, text = "1/x", padx = 14, pady = 10, command = button_1overx).grid(row=8, column=1)
        self.button_dashxdash = Button(self.buttons_frm_2, text = "|x|", padx = 17, pady = 10, command = button_dashxdash).grid(row=8, column=2)
        self.button_exp = Button(self.buttons_frm_2, text = "exp", padx = 14, pady = 10, command = button_exp).grid(row=8, column=3)
        self.button_mod = Button(self.buttons_frm_2, text = "mod", padx = 11, pady = 10, command = button_mod).grid(row=8, column=4)

        self.button_open = Button(self.buttons_frm_2, text = "(", padx = 21, pady = 10, command = button_open).grid(row=9, column=1)
        self.button_close = Button(self.buttons_frm_2, text = ")", padx = 21, pady = 10, command = button_close).grid(row=9, column=2)
        self.button_nexc = Button(self.buttons_frm_2, text = "n!", padx = 18, pady = 10, command = button_nexc).grid(row=9, column=3)

        #trig and function
        self.button_frig = Button(self.buttons_frm_1, text = "trigonometry", padx = 19, pady = 10, command = button_frig).grid(row=4, column=0, columnspan=2)
        self.button_func = Button(self.buttons_frm_1, text = "function", padx = 32, pady = 10, command = button_func).grid(row=4, column=2, columnspan=2)

        #M buttons
        self.button_Mc = Button(self.buttons_frm_1, text = "Mc", padx = 14, pady = 10, command = button_Mc).grid(row=3, column=0)
        self.button_Mr = Button(self.buttons_frm_1, text = "Mr", padx = 15, pady = 10, command = button_Mr).grid(row=3, column=1)
        self.button_Mplus = Button(self.buttons_frm_1, text = "M+", padx = 14, pady = 10, command = button_Mplus).grid(row=3, column=2)
        self.button_Mminus = Button(self.buttons_frm_1, text = "M-", padx = 15, pady = 10, command = button_Mminus).grid(row=3, column=3)
        self.button_MS = Button(self.buttons_frm_1, text = "MS", padx = 15, pady = 10, command = button_MS).grid(row=3, column=4)

        #top buttons
        self.button_FE = Button(self.buttons_frm_1, text = "F-E", padx = 14, pady = 10, command = button_FE).grid(row=2, column=0)
        self.button_RAD = Button(self.buttons_frm_1, text = "RAD", padx = 11, pady = 10, command = button_RAD).grid(row=2, column=1)
        self.button_GRAD = Button(self.buttons_frm_1, text = "GRAD", padx = 8, pady = 10, command = button_GRAD).grid(row=2, column=2)
        self.button_DEG = Button(self.buttons_frm_1, text = "DEG", padx = 12, pady = 10, command = button_DEG).grid(row=2, column=3)


    def create_GUI(self):
#        self.create_show_calculations()
        self.create_buttons()
        self.create_1_function_gui()

#Phase 1 powers
    def create_1_function_gui(self):
        self.button_power2 = Button(self.buttons_2_functions_1_frm, text = "x^2", padx = 13, pady = 10, command = button_power2)
        self.button_power2.grid(row = 8,column = 0)

        self.button_power3 = Button(self.buttons_2_functions_1_frm, text = "x^3", padx = 13, pady = 10, command = button_power3)
        self.button_power3.grid(row = 9,column = 0)

        self.button_powery = Button(self.buttons_2_functions_1_frm, text = "x^y", padx = 13, pady = 10, command = button_powery)
        self.button_powery.grid(row = 10,column = 0)

        self.button_10powerx = Button(self.buttons_2_functions_1_frm, text="10^x", padx = 10, pady = 10, command = button_10powerx)
        self.button_10powerx.grid(row=11, column=0)

        self.button_log = Button(self.buttons_2_functions_1_frm, text="log", padx = 15, pady = 10, command = button_log)
        self.button_log.grid(row=12, column=0)

        self.button_ln = Button(self.buttons_2_functions_1_frm, text="ln", padx = 18, pady = 10, command = button_ln)
        self.button_ln.grid(row=13, column=0)


#Phase 2 roots
    def create_2_function_gui(self):
        self.buttons_2_functions_2_frm = Frame(self, width=0, height=0, bg = "blue")#bg = "blue")
        self.buttons_2_functions_2_frm.grid(row = 8, column = 0)

        self.button_root2 = Button(self.buttons_2_functions_2_frm, text = "2√x", padx = 13, pady = 10, command = button_root2)
        self.button_root2.grid(row = 8,column = 0)

        self.button_root3 = Button(self.buttons_2_functions_2_frm, text = "3√x", padx = 13, pady = 10, command = button_root3)
        self.button_root3.grid(row = 9,column = 0)

        self.button_rooty = Button(self.buttons_2_functions_2_frm, text = "y√x", padx = 13, pady = 10, command = button_rooty)
        self.button_rooty.grid(row = 10,column = 0)

        self.button_twopowerx = Button(self.buttons_2_functions_2_frm, text="2^x", padx = 13, pady = 10, command = button_twopowerx)
        self.button_twopowerx.grid(row=11, column=0)

        self.button_logyx = Button(self.buttons_2_functions_2_frm, text="logyx", padx = 8, pady = 10, command = button_logyx)
        self.button_logyx.grid(row=12, column=0)

        self.button_epowerx = Button(self.buttons_2_functions_2_frm, text="e^x", padx = 13, pady = 10, command = button_epowerx)
        self.button_epowerx.grid(row=13, column=0)

    def mode_change(self):
        if self.modefunction == 1:
            self.buttons_2_functions_1_frm.destroy()
            self.modefunction = 2
            self.buttons_2_functions_2_frm = Frame(self, width=0, height=0)#bg = "blue")
            self.buttons_2_functions_2_frm.grid(row = 8, column = 0)
            self.create_2_function_gui()
        else:
            self.buttons_2_functions_2_frm.destroy()
            self.modefunction =  1
            self.buttons_2_functions_1_frm = Frame(self, width=0, height=0)#bg = "blue")
            self.buttons_2_functions_1_frm.grid(row = 8, column = 0)
            self.create_1_function_gui()

app = Calc(root)
root.mainloop()

def retrieve_input():
    try:
        global expression
        inputValue1 = InputA.get()
        inputValue2 = InputB.get()
        inputValue1 = float(inputValue1)
        inputValue2 = float(inputValue2)

        expression = float(math.sqrt(inputValue1 * inputValue1 + inputValue2 * inputValue2))
        equation.set(float(expression))
        expression = str(expression)

    except:
        equation.set(" Error ")
        expression = ""

'''print(pow(3,4))'''
