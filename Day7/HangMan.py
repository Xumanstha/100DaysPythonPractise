import random
from Hangman_arts import stages,logo2,logo3
from Hangman_word import word_list

# word_list=["aardvark","baboon","camel"]

lives=6

chosenword=random.choice(word_list)
print(logo3)
blankword=""

for letter in chosenword:
    blankword+="-"

print(blankword)

correct_letters=[]

game_over=False

while not game_over:
    guess=input("Guess a letter: ").lower()
    # print(guess)
    display=""

    if guess in correct_letters:
            print(f"You've already guessed {guess}")

    for char in chosenword:
        if guess==char:
            display+=char
            correct_letters.append(char)
        elif char in correct_letters:
            display+=char
        else:
            display+="-"
    
    

    if guess not in chosenword:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives==0:
            game_over=True
            print(f"******************IT WAS {chosenword} YOU LOSE******************")
    
            
    
    print(display)
    if "-" not in display:
        game_over=True
        print("******************YOU WIN******************")
        print(logo2)

    print(stages[lives])
   
       
