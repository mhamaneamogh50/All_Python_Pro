import random
gusess=[]
mycomputer = random.randint(1,99)
print("----------------------------------")
player=int(input("Enter number between 1-99 :-"))
gusess.append(player)
while player!= mycomputer:
    if player > mycomputer:
        print("----------------------------------")
        print("Number is higher !!!")

    else:
        print("----------------------------------")
        print("Numberis low !!!")

    player= int(input("Enter num 1-99"))

    gusess.append(player)

else:
    print("-----------------------------------")
    print(mycomputer)
    print("You have entered right number ---> ")
    print("Length --> %i "%len(gusess))
    print("Your number is ",gusess)
    
