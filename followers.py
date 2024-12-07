import random
from data1 import data2

def highlow(data1):
    print("WELCOME TO HIGHERLOWER GAME")
    rand_name1=random.choice(data2)
    score=0
    continue_game=True
    while continue_game:
        rand_name2=random.choice(data2)
        while rand_name1==rand_name2:
            rand_name1=random.choice(data2)
        name1,description1,country1,followers1=rand_name1['name'],rand_name1['description'],rand_name1['country'],rand_name1['follower_count']
        name2,description2,country2,followers2=rand_name2['name'],rand_name2['description'],rand_name2['country'],rand_name2['follower_count']
        print(f"COMPARE A:{name1} who is {description1} from {country1}")
        print("VS")
        print(f"COMPARE B:{name2} who is {description2} from {country2}")
        guess=input("Guess who has the highest followers?").upper()
        print (guess)
        if followers1>followers2 and guess == "A" or followers2>followers1 and guess =="B":
            score+=1
            print(f"you are going well with score {score}")
            if followers1>followers2:
                rand_name1=rand_name1
            else:
                rand_name1=rand_name2
        else:
            continue_game=False
            print(f"sorry, you are wrong. Your final score is {score}")
            

highlow(data2)










#TASK 1
#randomly generate name from data1
#the second name should be in loop until the first follower will win 
#if equal than again randomly generate
#provide the values of dictionary by keeping certain name
#conditional and score and print score
#determine and right the followers which is greater

#TASK 2
""" open git hub and create basics study material there and post the completed task and that study material.
go to day 16 of angelena yu and then aws"""


