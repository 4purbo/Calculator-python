from tkinter import *

#screen start
screen=Tk()
screen.title("Calculator")
screen.geometry('198x265')

# UI :

# variables :

global numList
numList=[]

# functions :

def button_add_f():
    numList.append(int(field.get()))
    field.delete(0,END)

def button(number):
    field.insert(END,number)
    global current_value

def button_clear_f():
    field.delete(0,END)
    numList.clear()

def button_equal_f():
    numList.append(int(field.get()))
    field.delete(0,END)
    result=0
    for i in numList:
        result+=i
    field.insert(0,result)
    numList.clear()

# buttons :

button1=Button(screen,text="1",padx=25,pady=15,command=lambda: button(1))
button2=Button(screen,text="2",padx=25,pady=15,command=lambda: button(2))
button3=Button(screen,text="3",padx=25,pady=15,command=lambda: button(3))

button4=Button(screen,text="4",padx=25,pady=15,command=lambda: button(4))
button5=Button(screen,text="5",padx=25,pady=15,command=lambda: button(5))
button6=Button(screen,text="6",padx=25,pady=15,command=lambda: button(6))

button7=Button(screen,text="7",padx=25,pady=15,command=lambda: button(7))
button8=Button(screen,text="8",padx=25,pady=15,command=lambda: button(8))
button9=Button(screen,text="9",padx=25,pady=15,command=lambda: button(9))

button0=Button(screen,text="0",padx=25,pady=15,command=lambda: button(0))

button_add=Button(screen,text="+",padx=25,pady=15,command=button_add_f)
button_equal=Button(screen,text="=",padx=25,pady=15,bg="green",command= button_equal_f)
button_clear=Button(screen,text="Clear",background="red",command=button_clear_f)

# input field and result field :
field=Entry(screen,borderwidth=1,width=30)
field.get()

# showing in the screen :
field.grid(row=0,column=0,columnspan=3)
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)

button0.grid(row=5,column=0)

button_add.grid(row=5,column=1)
button_equal.grid(row=5,column=2)
button_clear.grid(row=1,column=2)

#end
screen.mainloop()