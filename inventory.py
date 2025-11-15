items = []
prices = {}

while True:
    print("\n=== Inventory Menu ===")
    print("1. Add Item")
    print("2. Update Price")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Add Item ---")
        name = input("Enter item name: ").capitalize()

        if name in items:
            print("Error: Item already exists!")
            continue

        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("Invalid price. Must be a number.")
            continue

        items.append(name)
        prices[name] = price
        print("Item added successfully!")

    elif choice == "2":
        print("\n--- Update Item Price ---")
        name = input("Enter item name: ").capitalize()

        if name not in items:
            print("Error: Item not found!")
            continue

        try:
            new_price = float(input("Enter new price: "))
        except ValueError:
            print("Invalid price. Must be a number.")
            continue

        prices[name] = new_price
        print("Price updated successfully!")

    elif choice == "3":
        print("\n--- Inventory ---")
        if not items:
            print("Inventory is empty.")
        else:
            for item in items:
                print(f"{item} : ₱{prices[item]}")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
