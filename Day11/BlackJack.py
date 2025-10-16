import random
import art
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[]
banker_cards=[]

import random

def initialize():
    first_user_card = random.choice(cards)
    user_cards.append(first_user_card)

    first_banker_card = random.choice(cards)
    banker_cards.append(first_banker_card)

    second_user_card = random.choice(cards)
    user_cards.append(second_user_card)

    second_banker_card = random.choice(cards)
    banker_cards.append(second_banker_card)


def sum_the_cards(holder):
    sum_of_card = sum(holder)  # cleaner way to sum all cards

    if sum_of_card > 21 and 11 in holder:
        index = holder.index(11)
        holder[index] = 1
        return sum_the_cards(holder)  # return the recursive result
    else:
        return sum_of_card

def draw_card(hand):
    card=random.choice(cards)
    hand.append(card)

def check_BlackJack(hand):
    if sum(hand)==21:
        return True

def final_check(hand1,hand2):
    sumofcards1=sum(hand1)
    sumofcards2=sum(hand2)
    if sumofcards1>sumofcards2:
        if sumofcards1<21:
            print("You win!")
        else:
            print("You went over. Opponent win")
    elif sumofcards1==sumofcards2:
        print("Draw")
    else:
        if sumofcards2<21:
            print("Opponent win!")
        else:
            print("Opponent went over. You win")
            


def Black_Jack():
    if check_BlackJack(user_cards):
        print("You win BlackJack!")
        return
    print(f"Your cards {user_cards}, current score: {sum_the_cards(user_cards)}")
    print(f"Computer's first card: {banker_cards[0]}")
    choice=input("Type 'y' to get another card, type 'n' to pass: ")
    if choice == 'y':
        draw_card(user_cards)
        if check_BlackJack(user_cards):
            print(f"Your cards {user_cards}, current score: {sum_the_cards(user_cards)}")
            print("You win BlackJack!")
            user_cards.clear()
            banker_cards.clear()
            print("\n"*5)
            main()
        elif sum_the_cards(user_cards)>21:
            print(f"Your cards {user_cards}, current score: {sum_the_cards(user_cards)}")
            print("You went over. Opponent win!")
            user_cards.clear()
            banker_cards.clear()
            print("\n"*5)
            main()
        Black_Jack()
    else:
        print(f"Your final hand: {user_cards},final score: {sum_the_cards(user_cards)}")
        if check_BlackJack(banker_cards):
            print(f"Dealer cards {banker_cards}, current score: {sum_the_cards(banker_cards)}")
            print("Opponent win BlackJack!")
            user_cards.clear()
            banker_cards.clear()
            print("\n"*5)
            main()
        while sum_the_cards(banker_cards)<17:
            draw_card(banker_cards)
            if check_BlackJack(banker_cards):
                print(f"Your cards {banker_cards}, current score: {sum_the_cards(banker_cards)}")
                print("Opponent win BlackJack!")
                user_cards.clear()
                banker_cards.clear()
                print("\n"*5)
                main()
    print(f"Computer's final hand: {banker_cards}, final score: {sum_the_cards(banker_cards)}")
    final_check(user_cards,banker_cards)
    user_cards.clear()
    banker_cards.clear()
    print("\n"*5)
    main()

def main():
    choice=input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if choice == 'y':
        print(art.logo)
        initialize()
        Black_Jack() 

main()


        



    




