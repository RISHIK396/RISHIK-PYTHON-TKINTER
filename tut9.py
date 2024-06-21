from tkinter import *
root=Tk()

def print1():
    print(f"{uservalue.get()}")
    print(f"{passval.get()}")
root.geometry("600x600")
root.minsize(500,500)

user=Label(root,text="USER NAME:->",fg="black",bg="blue",borderwidth=3,relief=RIDGE).grid(row=0)
password=Label(root,text="PASSWORD:->",fg="black",bg="blue",borderwidth=3,relief=RIDGE).grid(row=3)

uservalue=StringVar
passval=StringVar

user_entry=Entry(root,textvariable=uservalue,fg="white",bg="black",font="serrif 15 bold",borderwidth=3,relief=SUNKEN).grid(row=0,column=2)
pass_entry=Entry(root,textvariable=passval,fg="white",bg="black",font="serrif 15 bold",borderwidth=3,relief=SUNKEN).grid(row=7,column=2)
button1=Button(text="SUBMIT",bg="grey",command=print1)
button1.grid(row=8,column=2)

root.mainloop()