from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Amogh")
L1=Label(root,text="Uname").grid(row=0,column=0)
L2=Label(root,text="Password").grid(row=1,column=0)
entry1=Entry(root).grid(row=0,column=1)
entry2=Entry(root).grid(row=1,column=1)
entry1.get()
entry2.get()
if(entry1=="a"):
    messagebox.showinfo("","Done")
    
root.mainloop()
