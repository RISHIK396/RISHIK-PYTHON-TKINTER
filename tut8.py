from tkinter import *
root=Tk()
root.title("THIS IS MY 8 TUTTORIAL OF TKINTER")
def hello():
    print("HELLO THIS IS A BUTTON YOU JUST CLICKED!!!")

root.geometry("500x500")
root.minsize(400,400)
root.maxsize(1200,1200)
# f1 =Frame(root,bg="grey",borderwidth=5,relief=SOLID)
# f1.grid(row=3)

label1=Label(root,text="HELLO TO MY TKINTER VIDEO",font="hellvatica 15 bold",bg="red",fg="white",borderwidth=5,relief= RAISED,pady=2)
label2=Label(root,text="WELCOME TO THE WORLD OF PYTHON GUI",background="yellow",fg="black",font="arial 10 bold underline",borderwidth=5,relief=SUNKEN,)
button1=Button(root,text="SUBMIT",fg="white",bg="black",borderwidth=4,relief=RIDGE,command=hello).grid(row=4,column=2)
label1.grid(row=1,column=2)
label2.grid(row=3)
root.mainloop()