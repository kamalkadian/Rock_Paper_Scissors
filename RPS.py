import random
print("~~~~~~~Welcome to Rock Paper Scissors~~~~~~~")
user_score=0
computer_score=0
ties=0
print()
name=input("Enter your name: ")
print()
while True:
    print("""Choices:
    1. for Rock enter 1
    2. For Paper enter 2
    3. For Scissors enter 3""")
    print()

    choice=int(input("Enter your choice: "))
    while (choice>3 or choice<1):
        choice=int(input("Enter the valid input: "))

    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_choice="Scissors"
    print()

    print("Your choice is: ",user_choice)
    print()

    print("~~~~~~Computer turn~~~~~~")
    computer=random.randint(1,3)

    if computer==1:
        com_choice="Rock"
    elif computer==2:
        com_choice="Paper"
    else:
        com_choice="Scissors"

    print("Computer choice is: ",com_choice)


    print("~~~~~~~Result~~~~~~")
    if ((user_choice=="Paper" and com_choice=="Rock") or (user_choice=="Rock" and com_choice=="Paper")):
        print("Paper Wins")
        result="Paper"
    elif ((user_choice=="Scissors" and com_choice=="Rock") or (user_choice=="Rock" and com_choice=="Scissors")):
        print("Rock wins")
        result ="Rock"
    elif (user_choice==com_choice):
        print("it is a tie")
        result="Tie"
    else:
        print("Scissors Wins")
        result = "Scissors"


    if result=="Tie":
        ties+=1
    elif result==user_choice:
        print("user wins")
        user_score+=1
    else:
        print("Computer wins")
        computer_score+=1

    print("~~~~~~~Scores~~~~~~~")
    print(name,"score is",user_score)
    print("computer's score is",computer_score)
    print("ties are",ties)
    print()

    repeat=input("to play again press any key else no? ")
    if repeat=="no" or repeat=="No":
        break
print("Game Over")
