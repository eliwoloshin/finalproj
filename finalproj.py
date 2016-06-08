"rock paper scissors::"

gametype = input("Press 1 to play the computer, press 2 to play a two player game.")

if gametype == 1:
    name = input("Please enter your name.")
    gamenumber = ("Hey "+name+", thanks for choosing to play the computer. How many games do you want to play? Make sure you choose an odd number.")
    gametype2 = input("Now, press 1 if you want to make the first move, or press 2 if you want the computer to make the first move.")
    if gametype2 == 1:
        move1 = input("Make your move: type in rock, paper or scissors to make your move")
        if move1 !== "rock" and move1 !== "paper" and move1 !== "scissors":
            print("Looks like you goofed that. Try again and be sure not to misspell the move you want to make.")
        elif move1 == "rock":
            print("The computer chose to put down paper. Looks like you lost.")
            game2 = input("If you want to play again, press 1. If not, press 2. Thanks for playing.")
            if game2 = input(
        elif move1 == "paper":
            print("The computer chose to put down scissors. Looks like you lost.")
        elif move1 == "scissors":
                print("The computer chose to put down rock. Looks like you lost.")
elif gametype2 == 2:
    name1 = input("Player 1, please enter your name.")
    name2 = input("Player 2, please enter your name.")
    print("Hey, "+name1+", look away from the computer so Player 1 can make his move without you seeing it.")
    p1move1 = input("Player 1, make your move by typing in either rock, paper or scissors.")
    print("Hey, "+name2+", look away from the computer so Player 2 can make his move without you seeing it.")
    p2move1 = input("Player 2, make your move by typing in either rock, paper or scissors.")