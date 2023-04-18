import random

user_wins = 0
computer_wins = 0

game_options = ["rock", "paper", "scissors"]
all_options = ["score", "rock", "paper", "scissors"]

while True:
    user_input = input("\nType Score for the Score\nType Quit to Quit\n\nRock/Paper/Scissors: ").lower()
    #quit
    if user_input == "score":
        #prints total wins
        print("You won ", user_wins, "times.")
        print("Computer won ", computer_wins, "times.")
        continue

    if user_input == "quit":
        #??
        #print("You won ", user_wins, "times.")
        #print("Computer won ", computer_wins, "times.")
        #print("Goodbye!")
        break

    #making sure input is valid
    if user_input not in all_options: 
        print("Not a valid input. Try again.")
        continue

    #rock:0 paper:1 scissors:2
    random_number = random.randint(0,2)

    #computers pick
    computer_pick = game_options[random_number]
    print("Computer picked", computer_pick + ".")

    #winning scenarios
    if user_input == "rock" and computer_pick == "scissors": 
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper": 
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock": 
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "paper": 
        print("You tied!")

    elif user_input == "rock" and computer_pick == "rock": 
        print("You tied!")

    elif user_input == "scissors" and computer_pick == "scissors": 
        print("You tied!")

    #any other option means user didn't win 
    else:
        print("You lost!")
        computer_wins += 1




