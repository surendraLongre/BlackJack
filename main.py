#import logo from art.py
from art import logo
import random


#start the game code
user_want=input("\nDo want to play a game of BlackJack? (y/n) ")
while user_want=='y':
    game_state='play'
    print(logo)
    hand='y'
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards=[]
    computer_cards=[]

    #get the cards and append them to the respective arrays
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))

    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    user_score=user_cards[0]+user_cards[1]
    computer_score=computer_cards[0]+computer_cards[1]



    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    hand=input("Do you want another hand? (y/n) ").lower()

    #get the user card values and get total score
    while hand=='y' and game_state=='play':
        choice=random.choice(cards)
        user_cards.append(choice)
        user_score+=choice
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score>21:
            for i in range(len(user_cards)):
                if user_cards[i]==11 and user_score>21:
                    user_cards[i]=1
                    user_score-=10
        if user_score>21:
            print(f"You got a bust")
            print(f"Your cards: {user_cards}, final score: {user_score}")
            print("You lost !!!!!!!!!!!!!!!!!")
            game_state='stop'
            exit

        if game_state=='play':
            hand=input("Do you want another hand? (y/n) ").lower()

    #get computer score 
    while computer_score<16:
        choice=random.choice(cards)
        computer_cards.append(choice)
        computer_score+=choice

        #check if computer got over 21
        if computer_score>21:
            for i in range(len(computer_cards)):
                if computer_cards[i]==11 and computer_score>21:
                    computer_cards[i]=1
                    computer_score-=10
        if computer_score>21:
            print(f"Computer got a bust")
            print(f"Your cards: {user_cards}, final score: {user_score}")
            print(f"Computer cards: {computer_cards}, final score: {computer_score}")
            print("You Won!!!!!!!!!!!!!!!!!!")
            game_state='stop'

    # if none of them got bust
    if game_state=='play':
        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {computer_cards}, final score: {computer_score}")
        if user_score==computer_score:
            print("draw!!!!!!!")
        elif user_score>computer_score:
            print("You Won!!!!!!!!!!!!!!!!!!")
        else:
            print("Computer Won!!!!!!!!!!!!!!")

    user_want=input("\nDo want to play a game of BlackJack? (y/n) ")

