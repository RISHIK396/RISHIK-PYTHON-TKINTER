from tkinter import *
root=Tk()
root.title("THIS IS SAMPLE GUI FOR PRACTISING THE CONCEPTS OF TKINTER")

def getval():
    print("YES YOR RESPONSE HAS BEEN RECORDED")
    print(f"{namevalue.get(),phoneval.get(),genderval.get(),emergencyval.get(),payment_modeval.get(),foodservicevalue.get()}")

    with open("records.txt","a")as f:
        f.write(f"{namevalue.get(),phoneval.get(),genderval.get(),emergencyval.get(),payment_modeval.get(),foodservicevalue.get()}")

root.geometry("500x500")
root.minsize(450,450)

#heading
Label(root,text="WELCOME TO HARRY TRAVELS",font="comicsans 15 bold",pady=10).grid(column=3)

#text labels
name=Label(root,text="NAME: ",fg="white",bg="black")
phone=Label(root,text="PHONE: ",fg="white",bg="black")
gender=Label(root,text="GENDER: ",fg="white",bg="black")
emergency=Label(root,text="EMERGENCY CONTACT: ",fg="white",bg="black")
payment=Label(root,text="PAYMENT MODE: ",fg="white",bg="black")


name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

##variables
namevalue=StringVar()
phoneval=StringVar()
genderval=StringVar()
emergencyval=StringVar()
payment_modeval=StringVar()
foodservicevalue=IntVar()

#creating entries
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phoneval)
genderentry=Entry(root,textvariable=genderval)
emergencyentry=Entry(root,textvariable=emergencyval)
paymententry=Entry(root,textvariable=payment_modeval)

# packing entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#Checkbox
foodservice=Checkbutton(text="want to prebook your meals",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

#button
Button(text="submit to harry travels",command=getval).grid(row=7,column=3)


root.mainloop()