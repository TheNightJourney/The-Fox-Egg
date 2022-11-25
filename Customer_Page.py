from Account import Account
from Bank import Bank
import os
import time


user_file = open('user_information.txt', 'rt')
general_data = user_file.readlines()


def customer_menu_panel(user):
    os.system('cls')
    global current_user
    global user_balance

    for line in general_data:
        specific_data = line.split(";")
        if user == specific_data[0]:
            current_user = user
            user_balance = specific_data[1]
            int(user_balance)

    print("== Welcome to the Fox's Egg Bank! ===\n"
          "=== What would you like to do? ===\n"
          "\n"
          "=== [0] Check Balance ===\n"
          "=== [1] Make a Deposit ===\n"
          "=== [2] Make a Withdrawal ===\n"
          "=== [3] Make a Payment ===\n"
          "=== [4] Quit Application ==="
          "\n")
    try:
        x = int(input("Enter a number: "))

        if x == 4:
            quit()

        if x == 0:
            check_balance()
            print("Another Transaction? [Y/N]"
                "\n")
            another = str(input("_"))
            another.lower()
            if another == "y":
                customer_menu_panel(user)
            else:
                quit()

        if x == 1:
            try:
                deposit_value = int(input("Enter the amount you'd like to deposit: "))
                if deposit_value > 0:
                    user_balance += deposit_value
                    str(user_balance)
                    for line_3 in general_data:
                        specific_data = line_3.split(";")
                        if user == specific_data[0]:
                            specific_data = specific_data.replace(specific_data[1], user_balance)
                    print("Deposit success.")
                    print("Another Transaction? [Y/N]"
                          "\n")
                    another = str(input("_"))
                    another.str.lower()
                    if another == "y":
                        customer_menu_panel(user)
                    else:
                        quit()
                else:
                    print("Invalid amount inputted. Please try again.")
                    customer_menu_panel(user)
            except ValueError:
                print("Invalid format inputted. Please use whole numbers.")
    except ValueError:
        print("Non-number entered. Try again.")
        time.sleep(3)
        customer_menu_panel(user)




def check_balance():
    print("Your current balance is", user_balance)


