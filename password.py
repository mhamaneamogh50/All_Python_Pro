import random
print("\t*********WELLCOME TO AUTOMATIC PASSWORD GENRATEOR*************")
print("\t                   #   #\n\t                   #   #\n\t                   #   # ")

print("\tWE DO NOT STORE ANY OF YOUR INFORMATION \n\tALL RIGHTS RESERVED BY****@Amogh****")
print("\n")
name= str(input("Enter Your Name :- "))
print("\n")
lower="abcdefghijkmnopqrstuvwxyz"
numbers = "012345678"
symbol = "@&*_"

all =  numbers + symbol + lower
length = 8
password = "".join(random.sample(all,length))
print("\n")
print(name,"Your Auto Generated Password Is:-",password)
print("\n\n ~~DO NOT SHARE YOUR PASSWORS WITH ANYONE~~ ")
