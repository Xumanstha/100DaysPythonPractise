import random
import art
play_game=True

def Check_number(guess_num,correct_num):
    if guess_num>correct_num:
        return "too high! \n"
    elif guess_num<correct_num:
        return "too low! \n"
    else:
        print(f"You got it! The answer was {correct_num} \n \n")
        return 0

def Guess_the_number():
    print("Welcome to the Number Guessing Game \n")
    print(art.logo)
    print("I'm thinking of a number between 1 and 100 \n")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard' ")

    game_number=random.randint(1,100)

    if difficulty=="easy":
        attempts=10
    else:
        attempts=5


    while attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number")
        player_number=int(input("Make a guess: "))
        if Check_number(player_number,game_number)==0:
           return
        else:
            print(Check_number(player_number,game_number))
            attempts-=1
        
        if attempts==0:
            print(f"You've run out of guesses. It was {game_number} Try again.\n \n")
            return
        else:
            print("Guess Again")

while play_game:
    Guess_the_number()
    print("Do you want to play the game again")
    choice=input("if yes type 'y' ")
    if choice!="y":
        print("Goodbye\n\n")
        play_game=False




