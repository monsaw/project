# IMPOORTATION OF MODULES SECTION 
from tkinter import *
import math

# SETTING UP THE WINDOW LIKE OF THE CALCULATOR
root=Tk()
root.title("MONSAW'S CALCULATOR")
root.resizable(0,0)
root.geometry("310x510")
my_frame = Frame(root, width = 300 , height = 500 )
my_frame.pack(side = TOP)

# Setting up the screen of the calculator
my_screen = Entry(my_frame , width = 40, borderwidth = 5)
my_screen.grid(row = 0 ,column = 1, columnspan = 4, padx = 5, pady = 30)

# THE FUNCTION SECTION ,
#  This funtion controls all the digits part of the calculator.
def botton_click(number):
    hold = my_screen.get()
    my_screen.delete(0,END)
    my_screen.insert(0, str(hold)+str(number))
   
# This function holds the functionality of clearing everything on the screen
def clear():
    my_screen.delete(0,END)

# This function holds the functionality of adding up  everything on the screen  
def add():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="add"
    general=addition
    my_buttondot.config( state = ACTIVE)

# This function holds the functionality of substraction in the calculator
def sub():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="sub"
    general=addition
    my_buttondot.config( state = ACTIVE)
# This function holds the functionality of multiplication in the calculator
def mul():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="mul"
    general=addition
    my_buttondot.config( state = ACTIVE)

# This function holds the functionality of division in the calculator
def div():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="div"
    general=addition
    my_buttondot.config( state = ACTIVE)

# This function is one of the integral part of the program, it carrries out  different operations based on certain conditions
def equal():
    global general,var
    number=float(my_screen.get())
    my_screen.delete(0,END)
    if var=="add":
        my_screen.insert(0, (general+number))

    if var=="sub":
        my_screen.insert(0, (general-number))

    if var=="mul":
        my_screen.insert(0, (general*number))
    
    if var=="div":
        my_screen.insert(0, (general/number))

    
# This function holds the functionality of mathematics square root in the calculator
def sqrt():
    sq=float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,sq**0.5)

# This function helps in dealing with the period (.) in float numbers and check for it's existence in a number before functioning
def dot():
    num=my_screen.get()
    my_screen.delete(0,END)
    my_screen.insert(0,(num +"."))
    if "." in str(my_screen.get()):
        my_buttondot.config(state=DISABLED)

# This function holds the functionality of math sin function in the calculator with some conversion techniques employed.
def Sin():
    sins= float(my_screen.get())*math.pi/180
    my_screen.delete(0,END)
    my_screen.insert(0,math.sin(sins))

# This function holds the functionality of math cos function in the calculator with some conversion techniques employed.
def Cos():
    sins= float(my_screen.get())*math.pi/180
    my_screen.delete(0,END)
    my_screen.insert(0,math.cos(sins))

# This function holds the functionality of math tan function in the calculator with some conversion techniques employed.
def Tan():
    sins= float(my_screen.get())*math.pi/180
    my_screen.delete(0,END)
    my_screen.insert(0,math.tan(sins))

# This function holds the functionality of deleting number from the back is it;mistakenly typed
def back():
    Back=str(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,(Back[:-1]))
    if "." not in str(my_screen.get()):
        my_buttondot.config(state=ACTIVE)

# This function holds the functionality of math sin inverse function in the calculator with some conversion techniques employed.
def ArcSin():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.asin(sins)/math.pi*180)

# This function holds the functionality of math cos inverse function in the calculator with some conversion techniques employed.
def ArcCos():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.acos(sins)/math.pi*180)

# This function holds the functionality of math tan inverse function in the calculator with some conversion techniques employed.
def ArcTan():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.atan(sins)/math.pi*180)

# This function holds the functionality of math log function in the calculator in base 10
def Log():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.log10(sins))

# This function holds the functionality of math anti-log function in the calculator 
def ALOG():
    new=float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,10**(new))

# BUTTON SECTION
# This section setting up the buttons to ne used in the program
my_button1 = Button(my_frame,text = "1" , padx= 20 , pady = 10, command = lambda : botton_click(1) )
my_button2 = Button(my_frame,text = "2" , padx= 20 , pady = 10, command = lambda : botton_click(2) )
my_button3 = Button(my_frame,text = "3" , padx= 20 , pady = 10, command = lambda : botton_click(3) )
my_button4 = Button(my_frame,text = "4" , padx= 20 , pady = 10, command = lambda : botton_click(4) )
my_button5 = Button(my_frame,text = "5" , padx= 20 , pady = 10, command = lambda : botton_click(5) )
my_button6 = Button(my_frame,text = "6" , padx= 20 , pady = 10, command = lambda : botton_click(6) )
my_button7 = Button(my_frame,text = "7" , padx= 20 , pady = 10, command = lambda : botton_click(7) )
my_button8 = Button(my_frame,text = "8" , padx= 20 , pady = 10, command = lambda : botton_click(8) )
my_button9 = Button(my_frame,text = "9" , padx= 20 , pady = 10, command = lambda : botton_click(9) )
my_button0 = Button(my_frame,text = "0" , padx= 20 , pady = 10, command = lambda : botton_click(0) )
my_buttondot = Button(my_frame,text = "." , padx= 22 , pady = 10, command = dot )
my_buttonequal = Button(my_frame,text = "=" , padx= 20 , pady =40, command = equal )
my_buttonadd = Button(my_frame,text = "+" , padx= 20 , pady = 10, command = add )
my_buttonsub = Button(my_frame,text = "-" , padx= 20 , pady = 10, command = sub )
my_buttonmult = Button(my_frame,text = "*" , padx= 21 , pady = 10, command = mul )
my_buttondiv = Button(my_frame,text = "/" , padx= 20 , pady = 10, command = div )
my_buttondsqrt = Button(my_frame,text = "Sqt" , padx= 20 , pady = 10, command = sqrt )
my_buttondclear = Button(my_frame,text = "Clear" , padx= 20 , pady = 10, command = clear )

my_buttonsin = Button(my_frame,text = " Sin " , padx= 20 , pady = 10, command = Sin )
my_buttoncos = Button(my_frame,text = " Cos " , padx= 20 , pady = 10, command = Cos )
my_buttontan = Button(my_frame,text = " Tan " , padx= 20 , pady = 10, command = Tan )
my_buttonback = Button(my_frame,text = " <-- " , padx= 20, pady = 10, command = back )

my_buttonarcsin = Button(my_frame,text = "ASin" , padx= 21 , pady = 10, command = ArcSin )
my_buttonarccos = Button(my_frame,text = "ACos" , padx= 20 , pady = 10, command = ArcCos )
my_buttonarctan = Button(my_frame,text = "ATan" , padx= 20 , pady = 10, command = ArcTan )
my_buttonlog = Button(my_frame,text = " Log" , padx= 20 , pady = 10, command = Log )

my_buttonAntilog = Button(my_frame,text = "ALOG" , padx= 20 , pady = 10, command = ALOG )


# This section puts all the button into the frame of the calculator and well positioning
my_buttonarcsin.grid(row=4,column = 4)
my_buttonarccos.grid(row=5,column=4)
my_buttonarctan.grid(row=6,column = 4)
my_buttonAntilog.grid(row=7,column = 4)

my_buttonsin.grid(row=1,column=4)
my_buttoncos.grid(row=2,column=4)
my_buttontan.grid(row=3,column=4)
my_buttonlog.grid(row=7,column=3)

my_button7.grid(row = 1, column = 1)
my_button8.grid(row = 1, column = 2)
my_button9.grid(row = 1, column = 3 ,pady = 10)

my_button4.grid(row = 2, column = 1 )
my_button5.grid(row = 2, column = 2)
my_button6.grid(row = 2, column = 3, pady = 10)

my_button1.grid(row = 3, column = 1,pady=10)
my_button2.grid(row = 3, column = 2)
my_button3.grid(row = 3, column = 3)

my_buttondot.grid(row = 4, column = 1)
my_button0.grid(row = 4 , column = 2)
my_buttonequal.grid(row = 4, column = 3 , rowspan = 2 )
my_buttondclear.grid(row=6 , column=3)
my_buttonadd.grid(row = 5, column = 1)
my_buttonsub.grid(row = 5 , column = 2)
my_buttonmult.grid(row = 6 , column = 1 , pady=10)
my_buttondiv.grid(row = 6 , column = 2)

my_buttondsqrt.grid(row= 7 , column = 2)
my_buttonback.grid(row = 7 , column = 1)

# THE EVENT LOOP SECTION THAT KEEPS THE CODE RUNNING 
root.mainloop()