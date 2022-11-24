def entry_function():
    print("""Welcome to The Fox's Egg Prototype Bank! Thank you for banking with us!\n
Would you like to login or register?
Enter [0] to register, and [1] to login.""")


def regis_or_log():
    initial_input = input("\nregister[0] or login[1]: ")
    try:
        if initial_input == "0":
            return textfile_reliant_register_function()
        elif initial_input == "1":
            return textfile_reliant_login_function()
        else:
            print("Error. Please try again.")
            return regis_or_log()
    except ValueError:
        return regis_or_log()


def textfile_reliant_login_function():
    decision_1 = input("Are you logging in as an admin or user? Press [0] for user, and [1] for admin: ")
    try:
        if decision_1 == "0":
            return user_login()
        elif decision_1 == "1":
            return admin_login()
        else:
            print("Error. Please try again.")
            return regis_or_log()
    except ValueError:
        return regis_or_log()


def user_login():
    username = input("Username: ")
    password = input("Password: ")
    for line in open("login_information.txt", "r").readlines():
        login_details = line.split(";")
        if username == login_details[0]:
            if password == login_details[1]:
                print("\nLogin success.")
                print("Welcome,", login_details[2], login_details[3])
                print("Thank you for your patronage.")
                return int(login_details[4])
            else:
                print("\n")
                print("Error in the username or password. Try again.")
                user_failed = input("Try again or register? [0] to try once more, and [1] to register: ")
                if user_failed == "0":
                   return textfile_reliant_login_function()
                elif user_failed == "1":
                    return textfile_reliant_register_function()
                else:
                    print("Error. Invalid input.")
                    return regis_or_log()


def admin_login():
    username = input("Username: ")
    password = input("Password: ")
    for line in open("admin_login_information.txt", "r"):
        login_details = line.split(";")
        if username == login_details[0]:
            if password == login_details[1]:
                print("\nLogin success.")
                print("Welcome,", login_details[2], login_details[3])
                print("Welcome to your administrator account.")
                return int(login_details[4])
            else:
                print("\n")
                print("Error in the username or password. Try again.")
                user_failed = input("Try again or register? [0] to try once more, and [1] to register: ")
                if user_failed == "0":
                    return textfile_reliant_login_function()
                elif user_failed == "1":
                    return textfile_reliant_register_function()
                else:
                    print("Error. Invalid input.")
                    return regis_or_log()


def textfile_reliant_register_function():
    # Take the user input for their data.
    admin_pass = str(input("To launch an admin account, enter the admin passcode: "))
    username = input("Enter the username you would like to use: ")
    password = input("Enter the password you would like to use: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    if admin_pass == "0":
        login_file = open("admin_login_information.txt", "a")
        login_file.write("\n")
        login_file.write(username)
        login_file.write(";")
        login_file.write(password)
        login_file.write(";")
        login_file.write(first_name)
        login_file.write(";")
        login_file.write(last_name)
        login_file.write(";")
        count = 0
        for line in login_file.readlines():
            count += 1
        new_count = count + 1
        int(new_count)
        login_file.write(new_count)
        login_file.close()
        print("Admin account creation success.")
        textfile_reliant_login_function()
    else:
        login_file = open("login_information.txt", "a")
        login_file.write("\n")
        login_file.write(username)
        login_file.write(";")
        login_file.write(password)
        login_file.write(";")
        login_file.write(first_name)
        login_file.write(";")
        login_file.write(last_name)
        login_file.write(";")
        count = 4000000
        for line in login_file.readlines():
            count += 1
        login_file.write(40000000 + int(count))
        print(count)
        login_file.close()
        print("User account creation success.")
        textfile_reliant_login_function()


