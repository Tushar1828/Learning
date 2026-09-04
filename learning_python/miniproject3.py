 #restaurnment management system
menu = {
    'BURGER' : 80,
    'PIZZA' : 120,
    'COFFEE': 70,
    'PASTA' : 120,
    'COFFEE' : 50,
    'ICE CREAME' : 50,
    'PATTIES' : 50,
    }
#GREET
print("welcome to PYTHON RESTAURANT")
print("BURGER : 80\nPIZZA : 120\nCOFFEE: 70\nPASTA : 120\nICE CREAME : 50")

order_total  = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item ? (yes/no)")
if another_order == "Yes":
    item_2  = input("Enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")  
    else:
        print(f"Order item {item_2} is not avaialable!")

print(f"The total amount of items to pay is {order_total}")                  