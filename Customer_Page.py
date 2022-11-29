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
        x = eval(input("Enter your choice: "))
        if x == 0:
            find_balance_function(user)
        if x == 1:
            add_balance_function(user)
        if x == 2:
            withdraw_balance_function(user)
        if x == 3:
            print("Unfortunately, the user transfer system\n"
                  "is still under construction. Please look\n"
                  "forward to that!")
            customer_decision()
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
    user_deposit = eval(input("Enter the amount you would like to deposit: "))

    data = []
    with open('user_information.txt', 'r') as file:
        data = file.readlines()

    for index, line in enumerate(data):
        if line.split(";")[0] == user:
            data[index] = f"{line.split(';')[0]};{str(int(line.split(';')[1]) + user_deposit)}\n"

    with open('user_information.txt', 'w') as file:
        file.writelines(data)

    print("Success. ")

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


def withdraw_balance_function(user):
    user_withdrawal = eval(input("Enter the amount you would like to withdraw: "))

    data = []
    with open('user_information.txt', 'r') as file:
        data = file.readlines()

    for index, line in enumerate(data):
        if line.split(";")[0] == user:
            data[index] = f"{line.split(';')[0]};{str(int(line.split(';')[1]) - user_withdrawal)}\n"

    with open('user_information.txt', 'w') as file:
        file.writelines(data)

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
