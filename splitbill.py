print("welcome to the calculator")
a=float(input("what was the total bill?"))
b=int(input("what percentage tip would you like to give? 10,12 or 15?"))
c=int(input("how many people to split bill?"))

totaltip=b/100*a
totalamount=totaltip+a
splitbill=totalamount/c

print(f"Total bill:{splitbill}")



