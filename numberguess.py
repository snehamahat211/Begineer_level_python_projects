import random
hard_level_lives=5
easy_level_lives=10
def level_chooser():
    level=input("choose your level easy or hard?: ")
    if level=="hard":
        return hard_level_lives
    else:
        if level=="easy": 
            return easy_level_lives
def number(guess_number,randomnumber,turns):
    if guess_number==randomnumber:
        print("congratulation you guessed the right number")
    else:
        if guess_number>randomnumber:
            print("TOOO HIGH")
            return turns-1
        
        if guess_number<randomnumber:
            print("TOOO LOWWWW")
            return turns-1
def game():
    print("Welcome to the number guessing game:")
    randomnumber=random.randint(1,100)
    # print("THE RANDOM NUMBER WE HAVE IS",randomnumber)
    turns=level_chooser()
    guess_number=0
    while guess_number!=randomnumber:
        print(f"You guessed number {guess_number} and have {turns} attempts to guess")
        guess_number=int(input("enter the number you guessed: "))
        turns=number(guess_number,randomnumber,turns)
        if turns==0:
            print("SORRY... YOU LOOSE")
            return
        elif guess_number!=randomnumber:
            print("Guess again")
game()
    

