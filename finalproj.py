"""
rock paper scissors::
name: Eli Woloshin
credit: http://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used/19747562#19747562
"""

import sys


#while answer.lower() != 'no':
gametype = int(input("Hi! This game is called rock, paper, scissors. Press 1 to play the computer, press 2 to play a two player game: "))

if gametype == 1:
    name = input("Please enter your name. ")
    gamenumber = int(input("Hey "+name+", thanks for choosing to play the computer. How many games do you want to play? Make sure you choose an odd number: "))
    if gamenumber%2==0:
        gamenumber = int(input("Looks like you made a mistake with that. Try again and be sure to put in an odd number this time."))
        if gamenumber%2==0:
            gamenumber = int(input("Looks like you made another mistake with that. Try again and be sure to put in an odd number this time. This is your last chance. "))
            if gamenumber%2==0:
                print("It looks like you're having some trouble thinking of odd numbers. This site might help you: http://www.aaamath.com/g25a2_x1.htm. After you've done some research, come on back and give this game another try. Good luck!")
                sys.exit()
    else:
        print("Nice choice!")
    move1 = input("Make your move: type in rock, paper or scissors. ")
    if move1 not in ["rock", "Rock", "paper", "Paper", "scissors", "Scissors", "scissor", "Scissor"]:
        move1 = input("Looks like you goofed that. Try again and be sure not to misspell the move you want to make.")
        if move1 not in ["rock", "Rock", "paper", "Paper", "scissors", "Scissors", "scissor", "Scissor"]:
            move1 = input("Looks like you goofed that again. Try again and be sure not to misspell the move you want to make. This is your last chance. ")
            if move1 not in ["rock", "Rock", "paper", "Paper", "scissors", "Scissors", "scissor", "Scissor"]:
                    print("It looks like you're having some trouble with your spelling. Do some research and come back later to try again.")
                    sys.exit()
    elif move1 in ["rock", "Rock"]:
        answer = input("The computer chose to put down paper. Looks like you lost. Do you want to play again? Give a yes or no answer. ")
    elif move1 in ["paper", "Paper"]:
        answer = input("The computer chose to put down scissors. Looks like you lost. Do you want to play again? Give a yes or no answer. ")
    elif move1 in ["scissors", "Scissors"]:
        print("The computer chose to put down rock. Looks like you lost.")
        answer = input("The computer chose to put down rock. Looks like you lost. Do you want to play again? Give a yes or no answer. ")
elif gametype == 2:
    name1 = input("Player 1, please enter your name.")
    name2 = input("Player 2, please enter your name.")
    p1move1 = input("Hey, "+name1+"! It's time for your turn. Make sure "+name2+" looks away before you go. Once they're looking away, make your move by typing in either rock, paper or scissors.")
    p2move1 = input("Hey, "+name2+"! It's time for your turn. Make sure "+name1+" looks away before you go. Once they're looking away, make your move by typing in either rock, paper or scissors.")
    if p1move1 == "rock" and p2move1 == "rock" or p1move1 == "paper" and p2move1 == "paper" or p1move1 == "scissors" and p2move1 == "scissors":
        p1move1 = input("Both of you played a rock, which means this round was a tie. You will both play again to break the tie. "+name1+", make your move by typing in rock, paper or scissors.")
        p2move2 = input(+name2+" it's your turn now. Make your move by typing in rock, paper or scissors. ")
        if p1move1 == "rock" and p2move1 == "rock" or p1move1 == "paper" and p2move1 == "paper" or p1move1 == "scissors" and p2move1 == "scissors":
            p1move1 = input("Both of you played a rock, which means this round was a tie. You will both play again to break the tie. "+name1+", make your move by typing in rock, paper or scissors.")
            p2move2 = input(+name2+" it's your turn now. Make your move by typing in rock, paper or scissors. ")
            if p1move1 == "rock" and p2move1 == "rock" or p1move1 == "paper" and p2move1 == "paper" or p1move1 == "scissors" and p2move1 == "scissors":
                answer = input("You tied again! It seems like you're pretty evenly matched. Do you want to play again? Give a yes or no answer. ")
    elif p1move1 == "rock" and p2move1 == "paper":
        answer = input(""+name1+" put down rock, and "+name2+" put down paper, so "+name1+" wins! Do you want to play again? Give a yes or no answer. ")
    elif p2move1 == "rock" and p1move1 == "paper":
        answer = input(""+name2+" put down rock, and "+name1+" put down paper, so "+name2+" wins! Do you want to play again? Give a yes or no answer. ")
    elif p1move1 == "rock" and p2move1 == "scissors":
        answer = input(""+name1+" put down rock, and "+name2+" put down scissors, so "+name1+" wins! Do you want to play again? Give a yes or no answer. ")
    elif p2move1 == "rock" and p1move1 == "scissors":
        answer = input(""+name2+" put down rock, and "+name1+" put down scissors, so "+name2+" wins! Do you want to play again? Give a yes or no answer. ")
    elif p1move1 == "scissors" and p2move1 == "paper":
        answer = input(""+name1+" put down scissors, and "+name2+" put down paper, so "+name1+" wins! Do you want to play again? Give a yes or no answer. ")
    elif p2move1 == "scissors" and p1move1 == "paper":
        answer = input(""+name2+" put down scissors, and "+name1+" put down paper, so "+name2+" wins! Do you want to play again? Give a yes or no answer. ")





    
    
    
    
    
    
    
    
    
    