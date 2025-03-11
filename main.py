
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""
import time
print("Welcome to the Elite 101 Chatbox!")
name = input("What is your name?: ")
age = (input("How old are you?: "))
print("Welcome " + name + "!! " + age + " is a wonderful age.")
time.sleep(2)
print("How can I help you?: ")
def display_menu():
    print("1. Return Item")
    print("2. Exchange Item")
    print("3. Help?")
    print("4. Exit\n")

display_menu()

def choice1():
    print("* We have a 30 day window to return items. \n* Items must be unused, in original packaging, and with tags attached. \n* Some items like personalized products, food, or software might not be eligible for returns. ")
def choice2():
    print("* We have a 30 day window to exchange items. \n* Items must be unused, in original packaging, and with tags attached. \n* Customers must present a receipt or other proof of purchase to process an exchange. \n* Fee will be charged if the customer is not exchanging for an item of equal value. ")
def choice3():
    print ("* Customer Service Phone Number - ### ### ####. \n* Customer Service Email - cs@gmail.com")
choice = int(input("Enter the number of your choice: "))
if choice == 1:
    print("Here are our Return Policies: ")
    choice1()
elif choice == 2:
    print("Here are our Exchange policies ")
    choice2()
elif choice == 3:
    print("Here is the phone number of our costumer service hotline!")
    choice3()
elif choice == 4:
    print("Thanks for chatting with me. Goodbye!!")
    exit()
