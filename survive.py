age=input("what is the current age of yours?\n")
days=365
weeks=52
months=12
age1=(int(age))
days1=90*365-365*age1
weeks1=90*52-52*age1
months=90*12-12*age1
print(f"you have {days1} days,{weeks1} weeks and {months} months")