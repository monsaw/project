from tkinter import *
import math
root=Tk()
root.title("My Calculator")
root.resizable(0,0)
my_screen = Entry(root , width = 40, borderwidth = 5)
my_screen.grid(row = 0 ,column = 1, columnspan = 4, padx = 5, pady = 30)


def botton_click(number):
    hold = my_screen.get()
    my_screen.delete(0,END)
    my_screen.insert(0, str(hold)+str(number))
   # 
    #my_buttondot = Button(root,text = "." , padx= 22 , pady = 10, command = dot )
   # my_buttondot.grid(row = 4, column = 1)


def clear():
    my_screen.delete(0,END)
    
def add():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="add"
    general=addition
    my_buttondot.config( state = ACTIVE)
    
def sub():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="sub"
    general=addition
    my_buttondot.config( state = ACTIVE)

def mul():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="mul"
    general=addition
    my_buttondot.config( state = ACTIVE)

def div():
    addition=float(my_screen.get())
    my_screen.delete(0,END)
    global general,var
    var="div"
    general=addition
    my_buttondot.config( state = ACTIVE)

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

    

def sqrt():
    sq=float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,sq**0.5)

def dot():
    num=my_screen.get()
    my_screen.delete(0,END)
    my_screen.insert(0,(num +"."))
    if "." in str(my_screen.get()):
        my_buttondot.config(state=DISABLED)

def Sin():
    sins= float(my_screen.get())*math.pi/180
    my_screen.delete(0,END)
    my_screen.insert(0,math.sin(sins))

def Cos():
    sins= float(my_screen.get())*math.pi/180
    my_screen.delete(0,END)
    my_screen.insert(0,math.cos(sins))

def Tan():
    sins= float(my_screen.get())*math.pi/180
    my_screen.delete(0,END)
    my_screen.insert(0,math.tan(sins))

def back():
    Back=str(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,(Back[:-1]))
    if "." not in str(my_screen.get()):
        my_buttondot.config(state=ACTIVE)

def ArcSin():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.asin(sins)/math.pi*180)

def ArcCos():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.acos(sins)/math.pi*180)


def ArcTan():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.atan(sins)/math.pi*180)


def Log():
    sins= float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,math.log10(sins))

def ALOG():
    new=float(my_screen.get())
    my_screen.delete(0,END)
    my_screen.insert(0,10**(new))
my_button1 = Button(root,text = "1" , padx= 20 , pady = 10, command = lambda : botton_click(1) )
my_button2 = Button(root,text = "2" , padx= 20 , pady = 10, command = lambda : botton_click(2) )
my_button3 = Button(root,text = "3" , padx= 20 , pady = 10, command = lambda : botton_click(3) )
my_button4 = Button(root,text = "4" , padx= 20 , pady = 10, command = lambda : botton_click(4) )
my_button5 = Button(root,text = "5" , padx= 20 , pady = 10, command = lambda : botton_click(5) )
my_button6 = Button(root,text = "6" , padx= 20 , pady = 10, command = lambda : botton_click(6) )
my_button7 = Button(root,text = "7" , padx= 20 , pady = 10, command = lambda : botton_click(7) )
my_button8 = Button(root,text = "8" , padx= 20 , pady = 10, command = lambda : botton_click(8) )
my_button9 = Button(root,text = "9" , padx= 20 , pady = 10, command = lambda : botton_click(9) )
my_button0 = Button(root,text = "0" , padx= 20 , pady = 10, command = lambda : botton_click(0) )
my_buttondot = Button(root,text = "." , padx= 22 , pady = 10, command = dot )
my_buttonequal = Button(root,text = "=" , padx= 20 , pady =40, command = equal )
my_buttonadd = Button(root,text = "+" , padx= 20 , pady = 10, command = add )
my_buttonsub = Button(root,text = "-" , padx= 20 , pady = 10, command = sub )
my_buttonmult = Button(root,text = "*" , padx= 21 , pady = 10, command = mul )
my_buttondiv = Button(root,text = "/" , padx= 20 , pady = 10, command = div )
my_buttondsqrt = Button(root,text = "Sqt" , padx= 20 , pady = 10, command = sqrt )
my_buttondclear = Button(root,text = "Clear" , padx= 20 , pady = 10, command = clear )

my_buttonsin = Button(root,text = " Sin " , padx= 20 , pady = 10, command = Sin )
my_buttoncos = Button(root,text = " Cos " , padx= 20 , pady = 10, command = Cos )
my_buttontan = Button(root,text = " Tan " , padx= 20 , pady = 10, command = Tan )
my_buttonback = Button(root,text = " <-- " , padx= 20, pady = 10, command = back )

my_buttonarcsin = Button(root,text = "ASin" , padx= 21 , pady = 10, command = ArcSin )
my_buttonarccos = Button(root,text = "ACos" , padx= 20 , pady = 10, command = ArcCos )
my_buttonarctan = Button(root,text = "ATan" , padx= 20 , pady = 10, command = ArcTan )
my_buttonlog = Button(root,text = " Log" , padx= 20 , pady = 10, command = Log )

my_buttonAntilog = Button(root,text = "ALOG" , padx= 20 , pady = 10, command = ALOG )
#my_buttonarctan = Button(root,text = "ATan" , padx= 20 , pady = 10, command = ArcTan )
#my_buttonlog = Button(root,text = " Log" , padx= 20 , pady = 10, command = Log )


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


root.mainloop()