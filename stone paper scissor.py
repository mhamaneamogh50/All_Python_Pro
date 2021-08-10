import random
game_list=['stone','paper','scissor']
computer = 0
user = 0
c=0
p=0

while(True):
    user=input("Enter Stone , Paper , scissor or Quit")
    computer=random.choice(game_list)

    if(user=="Quit"):
        break
    
    elif(user==computer):
        print('Tie')

    elif(user=='stone'):
        if(computer=='paper'):
            c=c+1
            print("computer won!!!")
        else:
            p=p+1
            print("Player Won !!!!")


    elif(user=='Paper'):
        if(computer=='Scissor'):
            c+=1
            print("Computer Won!")
        else:
            p+=1
            print("Player Won!")



    elif(user=='scissor'):
         if(computer=='stone'):
             c=c+1
             print("computer won!!!")
         else:
             p=p+1
             print("plyer won!!!")

    else:
        
        print("Incorrect Input")

    print(" ")
    print("player",p)
    print(" ")
    print("computer",c)
         
