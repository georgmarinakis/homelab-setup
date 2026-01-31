import random

def game():
    user = input("Enter your choice (rock, paper, scissors): ")
    
    myList = ['rock','paper','scissors']
    computer = random.choice(myList)
    print(f"The computer chose: {computer}")
    
    myDict = { "user_choice" : user, "computer_choice" : computer}
    return myDict

def compare_choices(user, computer):
    if user == computer:
        print("This is due!")
    if user == "rock":
        if computer == "paper":
            print("Paper covers rock. The computer wins!")
        else:
            print("Rock breakes scissors. The user wins!")
    if user == "paper":
        if computer == "scissors":
            print("Scissors cuts paper. The computer wins!")
        else:
            print("Paper covers rock. The user wins!")
    if user == "scissors":
        if computer == "rock":
            print("Rock breaks scissors. The user wins!")
        else:
            print("Scissors cuts paper. The user wins!")
    
game_var = game()
compare_choices(game_var["user_choice"], game_var["computer_choice"])
 