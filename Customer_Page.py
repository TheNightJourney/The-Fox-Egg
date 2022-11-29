import os


# To find the column size
total_size = os.get_terminal_size()
column_size = total_size.columns


def customer_menu_panel(user):
    os.system('cls')
    print("=== Welcome to the Fox's Egg Bank! ===\n"
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
            customer_decision(user)
        else:
            print("Unspecified number. Please try again.")
            customer_decision(user)
    except ValueError:
        print("Unknown variable inputted. Please try again.")
        customer_decision(user)


def find_balance_function(user):
    print("\n")
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
                os.system('cls')
                quit_function(user)
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

    print("Success.\n")

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
                os.system('cls')
                quit_function(user)
                quit()


def withdraw_balance_function(user):
    user_withdrawal = eval(input("Enter the amount you would like to withdraw: "))

    with open('user_information.txt', 'r') as file_check:
        balance_data = file_check.readlines()

    for balance_index, balance_line in enumerate(balance_data):
        if balance_line.split(";")[1] == user_withdrawal:
            data = []
            with open('user_information.txt', 'r') as file:
                data = file.readlines()

            for index, line in enumerate(data):
                if line.split(";")[0] == user:
                    data[index] = f"{line.split(';')[0]};{str(int(line.split(';')[1]) - user_withdrawal)}\n"

            print("\n")

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
                        quit_function(user)
        else:
            print("Balance not enough. Please try again.")
            customer_menu_panel(user)


def quit_function(user):
    # god i wish i don't regret this
    count = 0
    while count != 3:
        print("\n")
        count += 1
    layer_material = "______"
    count = 0
    other_count = 0
    print(layer_material.rjust(24, " "))
    print(layer_material.rjust(17, " "), layer_material.rjust(13, " "))
    print(layer_material.rjust(17, " "), layer_material.rjust(13, " "))
    print(layer_material.rjust(13, " "), layer_material.rjust(21, " "))
    print(layer_material.rjust(13, " "), layer_material.rjust(21, " "))
    while other_count != 4:
        print(layer_material.rjust(9, " "), layer_material.rjust(29, " "))
        other_count += 1
    other_count = 0
    print("\n=== Thank you for using the Fox's Egg! ===")
    print("\n    === See you again next time!! ===")
    while other_count != 4:
        print(layer_material.rjust(9, " "), layer_material.rjust(29, " "))
        other_count += 1
    print(layer_material.rjust(13, " "), layer_material.rjust(21, " "))
    print(layer_material.rjust(13, " "), layer_material.rjust(21, " "))
    print(layer_material.rjust(17, " "), layer_material.rjust(13, " "))
    print(layer_material.rjust(17, " "), layer_material.rjust(13, " "))
    print(layer_material.rjust(24, " "))
    while count != 3:
        print("\n")
        count += 1
    quit()
