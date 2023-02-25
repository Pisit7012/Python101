# สร้างตัวแปร
'''
name = " Pisit"
print(type(name))

friend = "Mhee"

print("Hi "+ friend +" How are you")

money = 10 
print(type(money))
print(friend+" Can you give "+str(money) + " bath for me?")

print('{} Can you give {} bath for me?'.format(friend,money))

print(f'{friend} Can you give {money} bath for me?')

m = 1234564687546
print(f'{m:,}')

print(f'{m:,.2f}')
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title("โปรแกรมบันทึกข้อมูล")
GUI.geometry('500x400')


def Button1():
    text = "300 บาท"
    messagebox.showinfo("เงินในบัญชี",text)

L1 = Label(GUI,text='โปรแกรทบันทักความรู้',font=("Angsana,30"),fg='green')
L1.place(x=200,y=100)
B1 = ttk.Button(GUI,text="เงินคงเหลือ",command=Button1)
B1.pack (ipadx=20,ipady=20)
B1.place(x=200,y=300)

def Button2():
    text = "500 บาท"
    messagebox.showinfo("เงินที่ต้องจ่าย",text)

FB1 = Frame(GUI)
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text="รายจ่าย",command=Button2)
B2.pack(ipadx=20,ipady=20)


GUI.mainloop()


