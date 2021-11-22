from random import choice, choices, randint
import time

# Number guessing game record (global so it saves when function resets)
record = 0

rpsfirsttime = True

balance = 5000



def gameselection():
    # Asks player what game they would like to play
    print("What would you like to do, " + name + "?")
    time.sleep(1)
    print("Currently, I am programmed with 4 options:")
    time.sleep(0.5)
    print("Enter '1' to play scissors-paper-rock")
    time.sleep(0.2)
    print("Enter '2' to play the number guessing game")
    time.sleep(0.2)
    print("Enter '3' to play the magic eight ball")
    time.sleep(0.2)
    print("Enter '4' to play the coin toss.")

    # Checks answer and runs the corresponding funciton
    answergiven = False
    while answergiven == False:
        answer = input()
        if answer == "1":
            rockpaperscissorsgame()
            answergiven = True
        elif answer == "2":
            numberguessinggame()
            answergiven = True
        elif answer == "3":
            magic8ball()
            answergiven = True
        elif answer == "4":
            if age >= 18:
                coinflip()
                answergiven = True
            else: 
                print("You are too young to gamble")
                print("please select either 1, 2 or 3")
        else: 
            print("please enter either 1, 2, 3 or 4")

def numberguessinggame():
    # number range
    number = randint(1, 100)
    tries = 0
    answerguessed = False
    global record

    # Introduction
    print("Let's play the number guessing game...")
    print("Do you know how to play?")
    playknowledge = input()

    # Game instructions
    if playknowledge == "no" or playknowledge == "n":
        print("ok. Here's how you play:")
        time.sleep(0.5)
        print("I'm currently thinking of a number between 1 and 100.")
        time.sleep(1.5)
        print("You input numbers, and I will tell you if my number is higher or lower")
        time.sleep(1.5)
        print("The aim of the game is to guess my number in the lowest number of guesses possible.")
        time.sleep(1.5)
    elif playknowledge == "yes" or playknowledge == "y":
        print("ok")
    else: print("Yes, or no, do you know how to play?")
    print("Let's begin. Input your guess here:")

    # Main game loop - checks if players number is higher or lower, then outputs this answer
    while answerguessed == False:
        try:
            guess = int(input())
            if guess < number: 
                print("higher")
                tries +=1
            elif guess > number: 
                print("lower")
                tries += 1
            elif guess == number: 
                tries += 1    
                print("you guessed it!")
                print("it took " + str(tries) + " guesses.")
                answerguessed = True

                if record == 0 or record > tries: 
                    record = tries
                print("Your record is: " + str(record))
                
        # avoid crashes if not entered an intager
        except ValueError: print("Please enter a number")

    # Ask player if they want to play again
    print("Do you want to play again?")
    answergiven = False
    while answergiven == False:
        answer = input()
        if answer == "yes" or answer == "y":
            answergiven = True
            numberguessinggame()
        elif answer == "no" or answer == "n":
            answergiven = True
            gameselection()
        else: print("Well? yes or no, do you want to play again?")

def rockpaperscissorsgame():
    global rpsfirsttime

    # Game instructions
    if rpsfirsttime == True:
        print("In this game, both of us select rock, paper or scissors")
        time.sleep(1)
        print("rock beats scissors, paper beats rock, and scissors beats paper")
        rpsfirsttime = False
    else:
        print("Let's begin!")

    # Choose an option for the computer
    computeroptions = ["ROCK", "PAPER", "SCISSORS"]
    computerselection = choice(computeroptions)

    # check what option the player selected
    while True:
        print("What is your selection? (R, P or S)")
        playerselection = input()
        if playerselection == "R" or playerselection == "r" or playerselection == "P" or playerselection == "p" or playerselection == "S" or playerselection == "s":
            break
        else: print("please input 'R', 'P', or 'S'")
    if playerselection == "R" or playerselection == "r":
        print("You chose rock. Rock versus...")
        playerselection = "ROCK"
    elif playerselection == "P" or playerselection == "p":
        print("You chose paper. Paper versus...")
        playerselection = "PAPER"
    elif playerselection == "S" or playerselection == "s":
        print("You chose scissors. Scissors versus...")
        playerselection = "SCISSORS"

    # Countdown to create suspense
    time.sleep(0.3)
    print("3")
    time.sleep(0.3)
    print("2")
    time.sleep(0.3)
    print("1")
    time.sleep(0.3)
    print(computerselection)

    # check for winner
    if computerselection == playerselection:
        print("It's a tie!")
    elif playerselection == 'ROCK' and computerselection == 'SCISSORS':
        print('You win!')
    elif playerselection == 'PAPER' and computerselection == 'ROCK':
        print('You win!')
    elif playerselection == 'SCISSORS' and computerselection == 'PAPER':
        print('You win!')
    elif playerselection == 'ROCK' and computerselection == 'PAPER':
        print('You lose!')
    elif playerselection == 'PAPER' and computerselection == 'SCISSORS':
        print('You lose!')
    elif playerselection == 'SCISSORS' and computerselection == 'ROCK':
        print('You lose!')
    
    # ask player if they want to play again
    print("Do you want to play again, " + name + "?")
    answergiven = False
    while answergiven == False:
        answer = input()
        if answer == "yes" or answer == "y":
            answergiven = True
            rockpaperscissorsgame()
        elif answer == "no" or answer == "n":
            answergiven = True
            gameselection()
        else: print("Well? yes or no, do you want to play again?")

def magic8ball():
    print("Enter your question below. If you wish to quit, enter 'Q'")
    
    # Options for answers
    answers = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",

    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",

    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",

    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

    # Check answer for quit, otherwise output an answer and rerun function
    question = input()
    answer = choice(answers)
    if question == 'Q' or question == 'q':
        gameselection()
    else: 
        print(answer)
        magic8ball()

def coinflip():
    global balance
    validanswer = False

    try:
        while validanswer == False:
            print("How much would you like to bet? You have " + str(balance) + " coins")
            bettingamount = int(input())
            if bettingamount > balance:
                print("You do not have that much money.")
            else:
                print("You bet " + str(bettingamount) + " coins.")
                validanswer = True
    except ValueError: print("Please enter a number")

    outcomes = ["heads", "tails", "side"]
    chance = [49, 49, 2]
    flip = choices(outcomes, chance,k=100)
    flipoutcome = choice(flip)

    if flipoutcome == "heads":
        print("you won!")
        print("you earned " + str(bettingamount) + " coins.")
        balance += bettingamount
        print("You now have " + str(balance) + " coins.")
    elif flipoutcome == "tails":
        print("You lost :(")
        balance -= bettingamount
        if balance < 0: 
            balance = 0
            print("You are now broke. No more gambling for you until I implement a way to get more money.")
        else: print("You now have " + str(balance) + " coins.")
    else: 
        print("The coin landed on it's side!")
        print("You win " + str(bettingamount * 25)  + " coins.")
        balance += bettingamount * 25
    
        # ask player if they want to play again
    print("Do you want to play again, " + name + "?")
    answergiven = False
    while answergiven == False:
        answer = input()
        if answer == "yes" or answer == "y":
            answergiven = True
            coinflip()
        elif answer == "no" or answer == "n":
            answergiven = True
            gameselection()
        else: print("Well? yes or no, do you want to play again?")


# TODO: implement gambling (e.g. blackjack, coinflip, slots)

# Introduction. Only runs once, at the start
# Asks for name, gives reply, then runs gameselection()
print("---")
print("")
print("")

print("hello.")
print("What is your name? ")
name = input()
print("hello " + name)
print("It's lovely to meet you")
print("How old are you?")
age = int(input())
print("Lovely.")

gameselection()