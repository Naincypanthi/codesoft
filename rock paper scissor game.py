import random
my_choice=int(input("enter your choice: type 0 for Rock, type 1 for Paper and type 2 for Scissors"))
computer_choice=random.randint(0,2)
print("computer_choice:")
print(computer_choice)
if my_choice<computer_choice:
    print("You Lose")
elif my_choice>computer_choice:
    print("you win")
elif my_choice==computer_choice:
    print("It's draw game")
elif computer_choice==0 and my_choice==2:
    print("Your lose")
elif computer_choice==2 and my_choice==0:
    print("Your win")
