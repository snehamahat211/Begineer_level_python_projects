import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ask_user=input("what is you ask_user?\n For rock-1\n For scissors-3\n For paper-2\n ")
if ask_user=="3":
    print(scissors)
elif ask_user=="2":
    print(paper)
elif ask_user=="1":
    print(rock)
computer=random.randint(1,3)
print(computer)
if computer==3:
    print(scissors)
elif computer==2:
    print(paper)
elif computer==1:
    print(rock)
if computer == int(ask_user):
    print("It's a tie!")
elif (computer == 1 and ask_user == "3") or \
     (computer == 3 and ask_user == "2") or \
     (computer == 2 and ask_user == "1"):
    print("You win!")
else:
    print("Computer wins!")