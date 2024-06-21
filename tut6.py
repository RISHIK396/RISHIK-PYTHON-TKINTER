from tkinter import *
from PIL import Image,ImageTk
tk1_root=Tk()
tk1_root.geometry("344x400")
tk1_root.minsize(300,300)
# tk1_root.maxsize(1200,1200)
image=Image.open("AVENGERS.jpg")
photo=ImageTk.PhotoImage(image)
label1=Label(image=photo)
label1.pack()
tk1_root.mainloop()