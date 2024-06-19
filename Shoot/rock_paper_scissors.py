#ROCK, PAPER, SCISSORS
import random

plays = ["ROCK", "PAPER", "SCISSORS"]

bot_names = ['Skye', 'Brad', 'Cas', 'Pi', 'Jess']

def bot_name():
    #Choosing a random bot name from the list of bot names
    
    bot_name = random.choice(bot_names)
    print(bot_name)
    return bot_name

def welcome(bot_name):
    #Asking for the player's name
    
    while True:
        name = input("Name of the player: ")
        if name.isalpha():
            print(f"Hey, {name}, I'm {bot_name}, nice to meet you. \nLet's play, ROCK, PAPER, SCISSORS")
            return name
        else:
            print("Enter a valid name: ")

def play():
    ##choosing a random play 

    bot_play = random.choice(plays)
    return bot_play.upper()


def checking_plays(bot_play,  bot_name):
    """ Allowing a player to shoot their play
     Also verifying who won, and asking to play again if the bot and the player chose the same play"""
    
    while True:
        play_with = input("ROCK? PAPER? SCISSORS? SHOOT!!: ").upper() 
        if play_with in plays:
             
            if play_with == "ROCK" in plays and bot_play == "SCISSORS" in plays:
                print(f"{bot_name} shot with {bot_play}. \nRock beats scissors, you WON!!")
                return bot_play
            elif play_with == "PAPER" in plays and bot_play == "ROCK" in plays:
                print(f"{bot_name} shot with {bot_play}. \nPaper beats rock, you WON!!")
                return bot_play
            elif play_with == "SCISSORS" in plays and bot_play == "PAPER" in plays:
                print(f"{bot_name} shot with {bot_play}. \nScissors beats paper, you WON!!")
                return bot_play
            elif play_with == "PAPER" in plays and bot_play == "ROCK" in plays:
                print(f"{bot_name} shot with {bot_play}. \nPaper beats rock, you WON!!")
                return bot_play
            elif play_with == bot_play:
                print("Try again")
            else:
                print(f"{bot_name} shot with {bot_play}. \nBetter luck next, time buddy. {bot_name} WON!")
                break
        else:
            print("Invalid play, play again")
            

if __name__ == "__main__":
    bot_name = bot_name()
    welcome(bot_name)
    bot_play = play()
    checking_plays(bot_play, bot_name)
