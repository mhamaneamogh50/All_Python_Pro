# My Dictionary project

from tkinter import *

#key down function
def click():
    entered_text=textentry.get() # this will collect the text form text entry box
    output.delete(0.0,END)
    try:
        defination=my_compdictionary[entered_text]
    except:
        defination="Sory ther is not such word in your Dictionayr!!!\nTry Again!!!"
    output.insert(END,defination)

### main:
window=Tk()
window.title("My Dictionary project")
window.configure(bg="Black")
photo1 = PhotoImage(file="C:\\Users\\amogh\\Pictures\\amogh11.PNG")
Label(window,image=photo1,bg="black") .grid(row=0,column=0,sticky=W)

#creat label
Label(window,text="DICTIONARY MADE BY AMOGH MHAMANE",bg="black",fg="white",font="Ariel 15 bold") .grid(row=1,column=0,sticky=W)
Label(window,text="Enter the word you would get defination for :-",bg="black",fg="white",font="Ariel 12 bold") .grid(row=2,column=0,sticky=W)
#creat a text entry box
textentry= Entry(window,width=40,bg="white")
textentry.grid(row=3,column=0,sticky=W)

#add a submit button
Button(window,text="SUBMIT\n",width=6,command=click) .grid(row=4,column=0,sticky=W)

#creat another label
Label(window,text="\n Defination:-",bg="black",fg="white",font="Ariel 12 bold").grid(row=5,column=0,sticky=W)
#creat a text box
output=Text(window,width=75,height=6,wrap=WORD,bg="white")
output.grid(row=6,column=0,columnspan=2,sticky=W)
#the dictionary
my_compdictionary={'amogh':'the name of creator','bug':'an faliuer of code'}

#exit label
#exit function

def close_window():
    window.destroy()
    exit()


#exit button
Button(window, text="exit", width=14,command=close_window) .grid(row=8,column=0,sticky=W)


####run the mainloop
window.mainloop()
