print("Welcome to the food ordering Chatbot!")
name = input("What is your name? ")
age = int(input("Hello " + name + " what is your age?"))
print("Welcome to the Food Ordering Service!\n")
print("Please choose a category:")
print("1. Pizza")
print("2. Burger")
print("3. Seafood")
print("4. Chinese Food")



def order_pizza():
    size = input("What size would you like(small, medium, or large?)")
    toppings = input("Enter the toppings you want separated by commas: ")
    print(f"\nYou ordered a {size} pizza with the following toppings: {toppings}.")
    print("Thank you for the order!")

def order_burger():
    burgertoppings=input("Enter which toppings you would like on your burger separated by commas.")
    fries_size=input("Would you like small, medium, or large fries?")
    drink=input("What kind of drink would you like?")
    print(f"\nYou ordered a burger with the following toppings: {burgertoppings}.")
    print(f"Fries size: {fries_size}, Drink: {drink}.")
    print("Thank you for your order!")

def order_seafood():
    print("\nYou chose Seafood!")
    print("Please choose from the following options:")
    print("1. Grilled Salmon")
    print("2. Shrimp")
    print("3. Lobster")

    seafood_choice = input("Enter the number of your choice: ")

    if seafood_choice == '1':
        print("\nYou ordered Grilled Salmon.")
    elif seafood_choice == '2':
        print("\nYou ordered Shrimp.")
    elif seafood_choice == '3':
        print("\nYou ordered Lobster.")
    else:
        print("Invalid choice. Returning to main menu.")
    print("Thank you for your order!")


def order_chinese_food():
    print("\nYou chose Chinese Food!")
    print("Please choose from the following options:")
    print("1. Kung Pao Chicken")
    print("2. Sweet and Sour Pork")
    print("3. Vegetable Lo Mein")

    chinese_choice = input("Enter the number of your choice: ")

    if chinese_choice == '1':
        print("\nYou ordered Kung Pao Chicken.")
    elif chinese_choice == '2':
        print("\nYou ordered Sweet and Sour Pork.")
    elif chinese_choice == '3':
        print("\nYou ordered Vegetable Lo Mein.")
    else:
        print("Invalid choice. Returning to main menu.")
    print("Thank you for your order!")



choice = input("Enter the number of your choice: ")

if choice == '1':
    order_pizza()
elif choice == '2':
    order_burger()
elif choice == '3':
    order_seafood()
elif choice == '4':
    order_chinese_food()
else:
    print("You have exited the menu. Please restart the program.")