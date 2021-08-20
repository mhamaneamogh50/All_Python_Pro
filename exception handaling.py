a=10
b=0
try:
    
    c=a/s
    print(c)
    print("------inside try-------")

except ZeroDivisionError as obj:
    print("divison by zero not allowed")
    print(obj)

except NameError as ob1:
    print(ob1)


else:
    print("insid else")

    

    
