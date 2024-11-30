import os
from asci import logocalculator
def add (n1,n2):
    return n1+n2
def subtract (n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide (n1,n2):
     return n1/n2

operations={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide,

    }

def calculator():
    print(logocalculator)
    num1=float(input("enter first number :  "))
    for symbol in operations:
        print(symbol)
    value=True
    while value:
        op_symbol=input("enter symbol that you want: ")
        num2=float(input("enter next number:"))
        calculate=operations[op_symbol]
        fanswer=calculate(num1,num2)
        print(f"{num1}+{num2}\n= {fanswer}")
        if input("if you want to continue the game than type 'YES' else 'NO'")=="yes".upper():
            num1=fanswer
        else:
            value=False
            if input("Do you want to calculate new numbers?")=="yes":
                calculator()
            else:
                print("GOOOD BYEE")
                break

calculator()
             




    