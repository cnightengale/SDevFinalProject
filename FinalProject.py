from tkinter import *
from tkcalendar import *

root=Tk()

root.geometry("400x700")
root.title("My Appointment Calendar")
root.configure(bg="purple")


def selectDate():
    myDate=mycal.get_date()
    selectedDate=Label(text=myDate, bg="orange")
    selectedDate.pack()

def myClick():
    myLabel = Label(root, bg="orange",text=message.get())
    myLabel.pack()
    message.delete(0, END)    

l=Label(root,text="Select M/D/YY for your appointment.", bg = "purple")
l.pack(pady=15)    

mycal=Calendar(root,setmode="day",date_pattern="m/d/yy")
mycal.pack()

open_cal=Button(root,text="Choose date selected ",command=selectDate)
open_cal.pack(pady=8)

l=Label(root,text="Enter appointment information and then select save.", bg = "purple")
l.pack()

message= Entry(root, width = 20, bg = "white", borderwidth = 4)
message.pack(ipady=2)

myButton = Button(root, text="Save", command = myClick, fg ="blue", bg = "yellow")
myButton.pack(pady=5)

exit = Button(root, text = "Exit", bg = "Red", command = exit)
exit.pack(padx=0, pady=2)

l=Label(root,text="___________________________________________________________", bg = "purple")
l.pack()

root.mainloop()
