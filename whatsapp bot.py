import pywhatkit

def whatsapp(num,message,hrs,mint):
    pywhatkit.sendwhatmsg(num,message,hrs,mint)

num=input("Enter the number at which message is to be sent : ")
num="+91"+num

message=input("Enter the message to be sent : ")

hrs=int(input("Enter the time in hours when the message is to be sent : "))

mint=int(input("Enter the time in minutes when the message is to be sent : "))

whatsapp(num,message,hrs,mint)   
