import random
def get_choices():
    player_choice = input("Enter your choice it can be(Rock, Paper,Scissors): ")
    options = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(options)
    choices = {"Player": player_choice, "Computer": computer_choice}
    return choices


def check_win(Player,Computer):
    print(f"You choose {Player} and Computer choose {Computer}")
    if Player==Computer:
        return "It's a tie!"
    elif Player=="Rock":
        if Computer =="Paper":
            return "Paper covers the Rock! Computer win!"
        else:
            return "Rock smashes the Scissors! You win!"
    elif Player=="Paper":
        if Computer =="Rock":
            return "Paper covers the Rock! You win!"
        else:
            return "Scissors cuts the Paper! Computer win!"
    elif Player=="Scissors":
        if Computer =="Paper":
            return "Scissors cuts the Paper! You win!"
        else:
            return "Rock smashes the Scissors! Computer win!" 

while True:
    choices = get_choices()
    Result = check_win(choices["Player"],choices["Computer"])
    print(Result)
    play = input("Do you want to play again: ")
    if play == 'no':
     break