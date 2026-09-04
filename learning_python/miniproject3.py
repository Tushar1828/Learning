 #restaurnment management system
menu = {
    'BURGER' : 80,
    'PIZZA' : 120,
    'COFFEE': 70,
    'PASTA' : 120,
    'ICE CREAME' : 50,
}
#GREET
print("welcome to PYTHON RESTAURANT")
print("BURGER : 80\nPIZZA : 120\nCOFFEE: 70\nPASTA : 120\nICE CREAME : 50")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added to your order")
    