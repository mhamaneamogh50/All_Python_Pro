from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window=Tk()
window.title("Login Page")
Label(window,text="UserName",font="ariel 12 bold").place(x=12,y=10)
Label(window,text="Password",font="ariel 12 bold").place(x=10,y=18)


global e1
global e2

e1=Entry(window)
e1.place(x=140,y=40)

e2=Entry(window)
e2.place(x=140,y=40)
e2.config(show="*")




def Ok():
    uname=e1.get()
    password=  e2.get()

    if(uname=="" and password==""):
        messagebox.showinfo("","Blank is not Allowed.")

    elif(uname=="Admin" and password=="12345"):
        messagebox.showinfo("","Login Successful.")

    else:
        messagebox.showinfo("","Login Failed.")


Button(window,text="Login",command=Ok,height=3,width=13).place(x=10,y=100)
        
window.mainloop()
