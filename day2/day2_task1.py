'''
chalenge 2: shopping cart calculator

problem 
to build a simple menu driven that
lets the user select product from a menu
calculate the total coast based on chose items
applies a 10% discount if the total cost is more than 100

display a producg menu
this program shows a list of availabe product with fixed price
exapmle

1. Apple - $2.50
2. Orange - $3.20
3. Banana - $1.50
4. Mango - $4.20

5. Exit


ouptut
1. Apple - $2.50
2. Orange - $3.20
3. Banana - $1.50
4. Mango - $4.20

5. Exit
select a product(1-4) or 5 to exit: 1
enter quantity of that product: 2
add 2* apple to cart = $5.00



'''

print("--- Welcome to the Shopping Cart ---")

products = {
    1: ("Apple", 2.50),
    2: ("Orange", 3.20),
    3: ("Banana", 1.50),
    4: ("Mango", 4.20)
}

cart = []
total = 0

while True:
    print("\nAvailable Products:")
    for key, value in products.items():
        print(f"{key}. {value[0]} - ${value[1]:.2f}")
    print("5. Exit")

    choice = int(input("\nSelect a product (1-4) or 5 to exit: "))

    if choice == 5:
        print("\n--- Your Cart Summary ---")
        if not cart:
            print("Your cart is empty.")
        else:
            for item in cart:
                print(f"{item[0]} x {item[1]} = ${item[2]:.2f}")
            print(f"\nSubtotal: ${total:.2f}")
            if total > 100:
                discount = total * 0.10
                total -= discount
                print(f"10% discount applied: -${discount:.2f}")
            print(f"Final Total: ${total:.2f}")
        print("Thank you for shopping with us!")
        break

    if choice in products:
        name, price = products[choice]
        qty = int(input(f"Enter quantity of {name}: "))
        item_total = price * qty
        total += item_total
        cart.append((name, qty, item_total))
        print(f"Added {qty} x {name} to cart = ${item_total:.2f}")
    else:
        print("Invalid choice, please select from 1 to 5.")
