import random
from asci import logoblackjack
import os
def deal_card():
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      card=random.choice(cards)
      return card
def calculate_score(cards):
      if sum(cards)==21 and len(cards)==2:
            return 0
      if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)  
      return sum(cards)
def compare(user_score,computer_score):
      if user_score==21 :
            print("you win")
      if computer_score==21 :
            print("computer win")
      elif user_score > 21:
            print("You went over 21. You lose.")
      elif computer_score > 21:
            print("Computer went over 21. You win!")
      elif user_score == computer_score:
            print("It's a draw.")
      elif user_score == 0:
            print("You have a Blackjack! You win!")
      elif computer_score == 0:
            print("Computer has a Blackjack! You lose.")
      elif user_score > computer_score:
            print("You win!")
      else:
            print("You lose.")
def play_game()  :   
      print(logoblackjack)
      user_card=[]
      computer_card=[]
      is_game_over=False

      for _ in range(2):
      #   newcard=deal_card()
      #   user_card.append(newcard)
            user_card.append(deal_card())
            computer_card.append(deal_card())
      while not is_game_over :
            user_score=calculate_score(user_card)
            computer_score=calculate_score(computer_card)
            print(f"your card:{user_card},current score:{user_score}")
            print(f"computer card:{computer_card[0]}")
            if user_score==0 or computer_score==0 or user_score>21:
                  is_game_over=True
            else:
                  user_should_deal=input("Type 'yes' to get another card and 'no' to pass ")
                  if user_should_deal=="yes":
                        (user_card.append(deal_card()))
                        
                  else:
                        is_game_over=True
      while computer_score!=0 and computer_score<17:
            computer_card.append(deal_card())
            computer_score=calculate_score(computer_card)
      print(f"Your final hand: {user_card}, final score: {user_score}")
      print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
      print(compare(user_score, computer_score))
while input("Do you want to play  card ?  yes or no= ")=="yes":
      os.system('clear')
      play_game()












            
      
      

      
      


