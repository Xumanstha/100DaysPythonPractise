import game_data
import random
import art

def draw_option():
    option=random.choice(game_data.data)
    return option

def Compare(count1,count2):
    if count1>count2:
        return True
    else:
        return False

def High_Low():
    print("Welcome to Higher Lower")
    print(art.logo2)
    score=0
    option_A=draw_option()
    option_B=draw_option()
    should_continue=True

    while option_B==option_A:
        option_B=draw_option()

    while should_continue:
        print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
        print(art.logo1)
        print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}\n\n")

        A_follower=option_A['follower_count']
        B_follower=option_B['follower_count']

        option=input("Who has more followers? Type 'A' or 'B' ")

        if option=="A":
            if Compare(A_follower,B_follower):
                score+=1
                print(f"You're right! Current score: {score}\n\n\n\n")
                option_A=option_B
                option_B=draw_option()
                while option_B==option_A:
                    option_B=draw_option()
            else:
                print(f"Sorry that's wrong Your final score is {score}\n\n\n\n")
                should_continue=False

        elif option=="B":
            if Compare(B_follower,A_follower):
                score+=1
                print(f"You're right! Current score: {score}\n\n\n\n")
                option_A=option_B
                option_B=draw_option()
                while option_B==option_A:
                    option_B=draw_option()
            else:
                print(f"Sorry that's wrong Your final score is {score}\n\n\n\n")
                should_continue=False

play_game=True
while play_game:
    choice=input("Do you want to play  Higher_Lower game type 'y' or 'n':  ")
    if choice=='y':
        High_Low()
    else:
        play_game=False


 