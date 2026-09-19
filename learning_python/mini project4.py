# BILLING SYSTEM

products = []

while True:
    print("\n ==== BILING SYSTEM ====")
    print("1. Add product")
    print("2. View Bill")
    print("3. calculate Total")
    print("4. Exit")

    choice =  input("ENter your choice: ")

# Add product

if choice == "1":

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("ENter quantity"))

    total = price * quantity

    product = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    products.append(product)

    print("product added succesfully !")