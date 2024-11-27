import random
from hangmanart import logo
print(logo)
from hangmanart import stages
from hangmanart import word_list

choice=random.choice(word_list)
print(choice)
word_len=len(choice)
print(word_len)
end_of_game=False
lives=6
display=[]
for _ in range(word_len):
    display+="_"

while not end_of_game :
    guess=input("Guess a random word")
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_len):
        letter=choice[position]
        print(letter)
        if letter==guess: 
            display[position]=letter
        
    if guess not in choice:
        print(f" You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("you win")
    print(stages[lives])

