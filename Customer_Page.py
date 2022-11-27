import os
import time


def customer_menu_panel(user):
    os.system('cls')
    print("== Welcome to the Fox's Egg Bank! ===\n"
          "=== What would you like to do? ===\n"
          "\n"
          "=== [0] Check Balance ===\n"
          "=== [1] Make a Deposit ===\n"
          "=== [2] Make a Withdrawal ===\n"
          "=== [3] Make a Payment ===\n"
          "=== [4] Quit Application ==="
          "\n")
    return customer_decision(user)


def customer_decision(user):
    try:
        x = int(input("Enter your choice: "))
        if x == 0:
            find_balance_function(user)
        if x == 1:
            add_balance_function(user)
        else:
            print("Unspecified number. Please try again.")
            customer_decision(user)
    except ValueError:
        print("Unknown variable inputted. Please try again.")
        customer_decision(user)


def find_balance_function(user):
    for line in open('user_information.txt').readlines():
        formatted_data = line.split(";")
        if formatted_data[0] == user:
            formatted_data[1].rstrip("\n")
            print("Your credit count is", formatted_data[1])
            x = input("Would you like to take another action? Please press [0] for Yes,\n"
                      "and anything else to quit the application: ")
            if x == "0":
                os.system('cls')
                return customer_menu_panel(user)
            else:
                print("Thank you for using the Fox's Egg Bank!\n"
                      "Hope to see you next time!")
                quit()


def add_balance_function(user):
    user_deposit = int(input("Enter the amount you would like to deposit: "))
    general_data = open('user_information.txt', 'a').readlines()
    for line_2 in general_data:
        general_data = line_2.split(";")
        if user_deposit > 0:
            if general_data[0] == user:
                general_data[0].rstrip("\n")
                int(general_data[1])
                general_data[1] += user_deposit
                print(general_data[1])
