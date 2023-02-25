from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title("information")
GUI.geometry('500x500')

Label(GUI, text='First name').grid(row=0)
Label(GUI, text='Last name').grid(row=1)
Label(GUI, text='ago').grid(row=2)
Label(GUI, text='height').grid(row=3)
Label(GUI, text='weight').grid(row=4)

e1=Entry(GUI)
e2=Entry(GUI)
e3=Entry(GUI)
e4=Entry(GUI)
e5=Entry(GUI)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)

def show_info():

    first_name = e1.get()
    last_name = e2.get()
    age = e3.get()
    height = float(e4.get())
    weight = float(e5.get())
    message = "First name: " + first_name + "\nLast name: " + last_name + "\nAge: " + age + "\nHeight: " + str(height) + "\nWeight: " + str(weight)
    messagebox.showinfo("Information", message)

Button(GUI, text='Show information', command=show_info).grid(row=5,column=1,pady=10)

def show_info():
    height = float(e4.get())
    weight = float(e5.get())
    a = height/100
    c=float(weight/(a**2))
    message2 = "Your BMI: " + "{:.2f}".format(c)
    messagebox.showinfo("Information", message2)
Button(GUI, text='Show Your BMI', command=show_info).grid(row=5,column=2,pady=10)

mainloop()