def entry_function():
    print("""Welcome to The Fox's Egg Prototype Bank! Thank you for banking with us!\n
Would you like to login or register?
Enter [0] to register, and [1] to login.""")


def regis_or_log():
    initial_input = input("\nregister[0] or login[1]: ")
    try:
        if initial_input == "0":
            return admin_vs_customer_register()
        elif initial_input == "1":
            return admin_vs_customer_login()
        else:
            print("Error. Please try again.")
            return regis_or_log()
    except ValueError:
        return regis_or_log()


def admin_vs_customer_login():
    avc_driver = input("To enter the admin account, enter the password. Otherwise, press any key: ")
    if avc_driver == "thefoxarrives":
        return admin_login_function()
    else:
        return customer_login_function()


def admin_vs_customer_register():
    avcr_driver = input("To create an admin account, enter the administrator password. "
                        "\nOtherwise, press any key: ")
    if avcr_driver == "thefoxarrives":
        return admin_register_function()
    else:
        return customer_register_function()


def admin_login_function():
    username = input("\nIf the username is entered incorrectly,"
                     "\nthe application will stop. Username: ")
    password = input("Password: ")
    for line in open("admin_information.txt", "r").readlines():
        login_details = line.split(";")
        if username == login_details[0]:
            if password == login_details[1]:
                print("\nLogin success.")
                print("Welcome,", login_details[2], login_details[3])
                print("This is your Bank Administration Account.")
                login_details[4].rstrip("\n")
                return str(login_details[0])
            else:
                print("Incorrect Password or Username.")
                user_failed = input("Try again or register? [0] to try once more, and [1] to register: ")
                if user_failed == "0":
                    admin_vs_customer_login()
                elif user_failed == "1":
                    admin_vs_customer_register()
                else:
                    print("Error. Invalid input.")
                    regis_or_log()


def customer_login_function():
    username = input("\nIf the username is entered incorrectly,"
                     "\nthe application will stop. Username: ")
    password = input("Password: ")
    for line in open("customer_login_information.txt", "r").readlines():
        login_details = line.split(";")
        if username == login_details[0]:
            if password == login_details[1]:
                print("\nLogin success.")
                print("Welcome,", login_details[2], login_details[3])
                print("Thank you for your patronage.")
                print(login_details[0])
                return str(login_details[0])
            else:
                print("Incorrect Password.")
                user_failed = input("Try again or register? [0] to try once more, and [1] to register: ")
                if user_failed == "0":
                    admin_vs_customer_login()
                elif user_failed == "1":
                    admin_vs_customer_register()
                else:
                    print("Error. Invalid input.")
                    regis_or_log()


def admin_register_function():
    # Take the user input for their data.
    username = input("Enter the username you would like to use: ")
    password = input("Enter the password you would like to use: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    for lines_in_admin in open('admin_information.txt', "r").readlines():
        reading = lines_in_admin.split(";")
        if username != reading[0]:
            continue
        if username == reading[0]:
            print("Username is taken. Please try again.")
            return customer_register_function()
    for lines_in_cust in open('customer_login_information.txt', "r").readlines():
        reading = lines_in_cust.split(";")
        if username != reading[0]:
            continue
        if username == reading[0]:
            print("Username is taken. Please try again.")
            return customer_register_function()
    login_file = open('customer_login_information.txt', 'a')
    login_file.write("\n")
    login_file.write(username)
    login_file.write(";")
    login_file.write(password)
    login_file.write(";")
    login_file.write(first_name)
    login_file.write(";")
    login_file.write(last_name)
    login_file.write(";")
    login_file.write("1")
    login_file.close()
    print("User account creation success. Be sure to restart the application.")
    quit()


def customer_register_function():
    # Take the user input for their data.
    username = input("Enter the username you would like to use: ")
    password = input("Enter the password you would like to use: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    for lines_in_cust in open('customer_login_information.txt', "r").readlines():
        reading = lines_in_cust.split(";")
        if username != reading[0]:
            continue
        if username == reading[0]:
            print("Username is taken. Please try again.")
            return customer_register_function()
    for lines_in_admin in open('admin_information.txt', "r").readlines():
        reading = lines_in_admin.split(";")
        if username != reading[0]:
            continue
        if username == reading[0]:
            print("Username is taken. Please try again.")
            return customer_register_function()
    login_file = open('customer_login_information.txt', 'a')
    login_file.write("\n")
    login_file.write(username)
    login_file.write(";")
    login_file.write(password)
    login_file.write(";")
    login_file.write(first_name)
    login_file.write(";")
    login_file.write(last_name)
    login_file.write(";")
    login_file.write("0")
    login_file.close()
    account_file = open("user_information.txt", "a")
    account_file.write("\n")
    account_file.write(username)
    account_file.write(";")
    account_file.write("50000")
    account_file.close()
    print("User account creation success. Please restart the application.")
    quit()
