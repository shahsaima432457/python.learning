# 🍽️ Restaurant Ordering System
# Step 1: Menu dictionary (item: price)
menu = {
    "Pizza": 200,
    "Burger": 120,
    "Pasta": 150,
    "French Fries": 100,
    "Coffee": 80,
    "Ice Cream": 90
}

# Step 2: Print welcome message and menu
print("🍴 Welcome to Saima's Restaurant 🍴")
print("\nHere is our menu:\n")
for item, price in menu.items():
    print(f"{item:15} - ₹{price}")

# Step 3: Create an empty cart
cart = {}

# Step 4: Take orders
while True:
    item = input("\nEnter the item you want to order: ").title()

    # Check if item exists in menu
    if item in menu:
        quantity = int(input(f"How many {item}s would you like? "))
        cart[item] = cart.get(item, 0) + quantity
        print(f"{quantity} {item}(s) added to your cart.")
    else:
        print("❌ Sorry, this item is not available.")

    # Step 5: Ask if they want to order more
    more = input("Do you want to order another item? (yes/no): ").lower()
    if more != "yes":
        break

# Step 6: Generate the bill
print("\n🧾 Generating your bill...\n")
total = 0
for item, quantity in cart.items():
    price = menu[item] * quantity
    total += price
    print(f"{item:15} x {quantity:<3} = ₹{price}")

print("-------------------------------")
print(f"Total Bill Amount: ₹{total}")
print("-------------------------------")
print("💖 Thank you for visiting Saima's Restaurant! 💖")
print("✨ Have a great day! ✨")
