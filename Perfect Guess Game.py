'''Game generates a random number and asks the user to guess it
    - If player's guess > actual number program displays "Lower number please"
    - If player's guess < actual number program displays "Higher number please
    - On correct guess, display the number of attempts'''


import random
random_num = random.randint(1,100)

No_of_Guess = 0

user_guess = True
 
def output(user_guess):
    
    global No_of_Guess
    

    while user_guess!= random_num:
        user_guess = int(input("Guess a number between 1 to 100: \n"))
        No_of_Guess += 1
    
        if user_guess == random_num:
            print("Correct guess")
            print(f"You guessed it in {No_of_Guess} chances")
        elif user_guess > random_num:
            print("Enter a smaller number")
        else:
            print("Enter a larger number")

output(user_guess)