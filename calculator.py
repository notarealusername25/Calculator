from tkinter import *

class Cal(Frame):
    def __init__(self, maste):
        self.modefunctio = 1
        """ Initialize the frame. """
        super(Cal,self).__init__(maste)
        self.grid()

        self.buttons_fr = Frame(self, width= 0, height=0,bg = "red",padx=1, pady =1)#bg = "green")
        self.buttons_fr.grid(row = 0, column = 0)

        self.buttons_2_functions_1_fr = Frame(self, width=0, height=0,bg = "blue")#bg = "blue")
        self.buttons_2_functions_1_fr.grid(row = 1, column = 0, columnspan=2)
        self.create_GU()

    #def create_show_calculations(self):
        #self.calculation_lbl = Label(self.calculations_frm, text = "will show caluclations here").pack()

    def create_button(self):
        #mc stands for mode change
        self.mode_change_bt = Button(self.buttons_fr, text = "trig", command = self.mode_chang, padx = 19, pady = 10)
        self.mode_change_bt.grid(row =0,column =0)

        #self.plus_btn = Button(self.buttons_frm, text = "plus", height = 1, width = 5)
        #self.plus_btn.grid(row = 1,column = 0)

    def create_GU(self):
        #self.create_show_calculations()
        self.create_button()
        self.create_1_function_gu()


    def create_1_function_gu(self):
        self.sin_bt = Label(self.buttons_2_functions_1_fr, text = "x", padx = 19, pady = 10)
        self.sin_bt.grid(row = 1, column = 0)

        self.cos_bt = Label(self.buttons_2_functions_1_fr, text = "y", padx = 19, pady = 10)
        self.cos_bt.grid(row = 1, column = 1)

        self.cos_bt = Label(self.buttons_2_functions_1_fr, text="z", padx=19, pady=10)
        self.cos_bt.grid(row=1, column=2)


    def create_2_function_gu(self):
        """stop"""
        class Calc(Cal):
            def __init__(self, master):
                self.modefunction = 1
                super(Calc, self).__init__(master)
                self.grid()

                self.buttons_frm = Frame(self, width=0, height=0, bg="red", padx=1, pady=1)
                self.buttons_frm.grid(row=2, column=0)

                self.buttons_2_functions_1_frm = Frame(self, width=0, height=0, bg="blue")
                self.buttons_2_functions_1_frm.grid(row=2, column=1)
                self.create_GUI()

            def create_buttons(self):
                self.mode_change_btn = Button(self.buttons_frm, text="2nd", command=self.mode_change, padx=19, pady=10)
                self.mode_change_btn.grid(row=0, column=0)

            def create_GUI(self):
                self.create_buttons()
                self.create_1_function_gui()

            def create_1_function_gui(self):
                self.sin_btn = Button(self.buttons_2_functions_1_frm, text="sin", padx=19, pady=10)
                self.sin_btn.grid(row=0, column=0)

                self.cos_btn = Button(self.buttons_2_functions_1_frm, text="cos", padx=19, pady=10)
                self.cos_btn.grid(row=0, column=1)

            def create_2_function_gui(self):
                self.buttons_2_functions_2_frm = Frame(self, width=0, height=0)  # bg = "blue")
                self.buttons_2_functions_2_frm.grid(row=0, column=0)

                self.inverse_sin_btn = Button(self.buttons_2_functions_2_frm, text="sin-1", padx=19, pady=10)
                self.inverse_sin_btn.grid(row=0, column=1)

                self.inverse_cos_btn = Button(self.buttons_2_functions_2_frm, text="cos-1", padx=19, pady=10)
                self.inverse_cos_btn.grid(row=4, column=2)

            def mode_change(self):
                if self.modefunction == 1:
                    self.buttons_2_functions_1_frm.destroy()
                    self.modefunction = 2
                    self.buttons_2_functions_2_frm = Frame(self, height=0, width=0)  # bg = "blue")
                    self.buttons_2_functions_2_frm.grid(row=2, column=0)
                    self.create_2_function_gui()
                else:
                    self.buttons_2_functions_2_frm.destroy()
                    self.modefunction = 1
                    self.buttons_2_functions_1_frm = Frame(self, height=0, width=0)  # bg = "blue")
                    self.buttons_2_functions_1_frm.grid(row=2, column=1)
                    self.create_1_function_gui()


    def mode_chang(self):
        if self.modefunctio == 1:
            self.buttons_2_functions_1_fr.destroy()
            self.modefunctio = 2
            self.buttons_2_functions_2_fr = Frame(self, height = 0, width = 0)#bg = "blue")
            self.buttons_2_functions_2_fr.grid(row = 2, column = 0)
            self.create_2_function_gu()
        else:
            self.buttons_2_functions_2_fr.destroy()
            self.modefunctio =  1
            self.buttons_2_functions_1_fr = Frame(self, height = 0, width = 0)#bg = "blue")
            self.buttons_2_functions_1_fr.grid(row = 2, column = 0)
            self.create_1_function_gu()

root = Tk()
root.title("booking system")
root.geometry("500x500")
root.configure(bg="white")
app = Cal(root)

root.mainloop()
