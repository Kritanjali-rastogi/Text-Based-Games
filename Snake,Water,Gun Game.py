# Snake water gun game requires two players both have to select something from snake or water or gun
'''Game Rules:
                1. Snake wins over water
                2. Gun win over snake
                3. Water wins over gun'''
# Player with maximum points wins the game
# In the code, Player 1 will be computer while Player 2 will be a user

print("Welcome to snake, water, gun game")

import random

random_no = random.randint(1,3)

if random_no==1:
    choice_player1 = "Snake"
elif random_no==2:
    choice_player1 = "Water"
else:
    choice_player1 = "Gun"

print("The computer has chosen, now your turn")

choice_player2 = input("Enter one: 'Snake', 'Water', 'Gun': \n")

def game_winner(choice_player2):

    if choice_player1 == choice_player2:
        return None
    else:
        if choice_player1 == "Snake":
            if choice_player2 == "Water":
                return False
            elif choice_player2 == "Gun":
                return True
        if choice_player1 == "Water":
            if choice_player2 == "Snake":
                return True
            elif choice_player2 == "Gun":
                return False
        if choice_player1 == "Gun":
            if choice_player2 == "Snake":
                return True
            elif choice_player2 == "Water":
                return False

winner = game_winner(choice_player2)

print(f"The computer's choice was: {choice_player1} ")
print(f"You Choose: {choice_player2} ")

if winner == None:
    print("The game was a tie")
elif winner == True:
    print("Congratulation, You won")
else:
    print("Sorry, you lost. Better luck next time")