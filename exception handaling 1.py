a=10
b=0
try:
    c=a/b
    print(c)

except (NameError,ZeroDivisionError):
    print("Exception handler")
q=1
w=2
e=q+w

print(e)
