# Labels and pack in python tkinter
from tkinter import *
root1=Tk()
root1.geometry("1200x1200")
root1.title("MY GUI USING TKINTER")

# IMPORTANT LABEL OPTIONS
title_label=Label(text="hello world welcome to the world of Tkinter",bg="red",fg="white",padx=113,pady=94,font="comicsans,19,bold",borderwidth=3,relief=RAISED)
# title_label.pack(side=BOTTOM,anchor="sw",fill=X)
title_label.pack(side=LEFT,fill=Y)
root1.mainloop()
