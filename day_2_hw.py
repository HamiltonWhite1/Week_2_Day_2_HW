###EXERCISE 3
# 1) Build a Shopping Cart
# Should have the following capabilities:
# 1) Takes in input
# 2) Stores user input into a list
# 3) User can add or delete items
# 4) User can see current shopping list
# 5) Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

def shopping_cart():
    cart = []
    done = True
    yes_no = ["Y", "N"]
    yes_or_no = input("Would you like to go shopping? Y/N: ").upper()
    while done:
        if yes_or_no in yes_no:
            if yes_or_no == "Y":
                item = input("What would you like to add to your cart?: ").title()
                cart.append(item)
                keep_going = input("Would you like to keep shopping? Y/N: ").upper()
                yes_or_no = keep_going
            else:
                quit_y_n = input("Would you like to quit the program? Y/N: ").upper()
                if quit_y_n == "Y":
                    done = False
                else:
                    yes_or_no = "Y"
                    continue
        elif yes_or_no not in yes_no:
            print("Sorry, that was not an option. Try again.")
            quit_y_n = input("Would you like to quit the program? Y/N: ").upper()
            if quit_y_n == "Y":
                done = False
                break
            else:
                yes_or_no = "Y"
                continue
    see_cart = input("Would you like to see what is in your cart? Y/N: ").upper()
    if see_cart in yes_no:
        if see_cart == "Y":
            print(cart)
    delete_in_cart = input("Would you like to delete anything in your cart? Y/N: ").upper()
    if delete_in_cart in yes_no:
        if delete_in_cart == "Y":
            what_delete = input(f"Here is your cart {cart}. What would you like to delete?: ").title()
            if what_delete in cart:
                cart.remove(what_delete)
    anything_else = input("Would you like to add anything else? Y/N: ").upper()
    if anything_else in yes_no:
        if anything_else == "Y":
            done = True
    print(cart)
shopping_cart()



###EXERCISE 2
# 2) Create a Module in Visual Studio Code and Import It
# Module should have the following capabilities:
# 1) Has a function to calculate the square footage of a room
# 2) Has a function to calculate the circumference of a circle
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage

# from math_functions import squareft_room, circumference

# def solve_for_room_or_circle():
#     choices = ["ROOM", "CIRCLE"]
#     choice = input("Would you like to solve the circumference of a circle, or the squarefootage of a room? room/circle: ").upper()
#     solving = True
#     if choice in choices:
#         while solving:
#             if choice == "ROOM":
#                 length = int(input("What is the length?: "))
#                 width = int(input("What is the width?: "))
#                 return squareft_room(length, width)
#             elif choice == "CIRCLE":
#                 radius = int(input("What is the radius?: "))
#                 return circumference(radius)
#             solving = False
#     else:
#         print("That was not an option to choose from. Please try again.")
# print(solve_for_room_or_circle())
