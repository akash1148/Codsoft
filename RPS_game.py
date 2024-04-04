# Task 3: Rock, Paper, Scissors Game


import random

print("Welcome to the Rock Paper Sciccors GAme\n")

def game(u,c):
    print("Select One:\nrock\npaper\nscissors\n------------------\n")
    a=input("Your Choice:")

    options="rock","paper","scissors"
    b=random.choice(options)
    print("------------------")

    print("Computer CHoice:",b,"\n")
    
    if(a==b):
        print("Draw, YOu Both selected Same.\n")
    elif(a=="rock"):
        if(b=="scissors"):
            print("YOU Win:\n Rock Beats Scissors")
            u += 1
        else: 
            print("You lose:\n Paper Beats Rock")
            c += 1
            
    elif(a=="scissors"):
        if(b=="paper"):
            print("YOU Win:\n Scissors Beats Paper")
            u += 1
        else: 
            print("You lose:\n Rock Beats Scissors")
            c += 1
            
            
    elif(a=="paper"):
        if(b=="rock"):
            print("YOU Win:\n Paper Beats Rock")
            u += 1
        else: 
            print("You lose:\n Scissors Beats Paper")
            c += 1
            
    choice=input("Do YOu want to play Another Round?\nIf Yes press 1\nIf NO press -1\n")
    print("------------------")

    if(choice=="1"):
        game(u,c)
    elif(choice=="-1"):
        result(u,c)
        exit()      
    
            

def result(u,c):
    if(u>c):
        print("Congratulation you win the Game by",u,"-",c)
    elif(u==c):
        print("Game Draw by",u,"-",c)
    else:
        print("Unfortunately, You Lose The Game BY",u,"-",c)

game(0,0)

