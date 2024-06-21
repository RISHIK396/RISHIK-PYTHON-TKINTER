#writing a tkinter
from tkinter import *
from PIL import Image,ImageTk
tk1_root=Tk()
tk1_root.geometry("1200x1400")

# for jpg files
image=Image.open("AVENGERS.jpg")
photo=ImageTk.PhotoImage(image)
# photo=PhotoImage(file="AVENGERS.jpg")
rishik1=Label(image=photo)
rishik1.pack()
rishik2=Label(text="AVENGERS ASSEMBLE")
rishik2.pack()
tk1_root.mainloop()