print("LETS BEGIN WITH OUR GAME\n\n")
print("Welcome to the treasure ishand.Your mission is to find the treasure ")
print("you are in the middle of jungle.you have to find right choices in game to win tressure.so,choose your way wisely")
direction=input("choose between'right'or 'left'")
if direction=="right":
    print("ohhhhh shit....you are haunted by animal \n Game over")
elif direction=="left":
    choice=input("choose between 'swim' or 'wait'")
    if choice=="swim":
        print(" yor are drown :( game over")
    elif choice=="wait":
        choice1=input("choose between doors 'Red'  or 'green' or 'yellow' ")
        if choice1=="red":
            print("you have chose rightpath .you are in the middle of beautigul garden.there is axe next to you.")
            print("use axe and destroy the wooden box.you will find treasure there.")
        elif choice1=="green":
            print("you have chosen wrong way")
            print("GAME OVER")
        elif choice1=="yellow":
            print("you have chosen wrong way")
            print("GAME OVER")
        

                           
