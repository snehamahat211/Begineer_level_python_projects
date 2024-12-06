Menu={'pizza':350,
      'mo:mo':150,
      'pasta':150,
      'Burger':150,
      'salad':120,
      }
print("Welcome to the python restaurant")
print("'pizza':350 \n 'mo:mo':150 \n 'pasta':150 \n'Burger':150 \n'salad':120 \n")
order_item=0
while True:
    item=input("Name the item you want to order:").lower()
    if item in Menu:
        order_item+=Menu[item]
        print(f"your item {item} has been added to the list")
    else:
        print("Sorry...we dont have this item")
    another_order=input("Do you want next order? (y/n):")
    if another_order!="y":
        break
print(f"The total amount to pay is Rs {order_item}")
