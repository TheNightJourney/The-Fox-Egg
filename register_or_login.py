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
    username = input("Username: ")
    password = input("Password: ")
    for line in open("login_information.txt", "r").readlines():
        login_details = line.split(";")
        if username == login_details[0]:
            if password == login_details[1]:
                print("\nLogin success.")
                print("Welcome,", login_details[2], login_details[3])
                if int(login_details[4]) == 1:
                    print("This is your Bank Administration Account.")
                elif int(login_details[4]) == 0:
                    print("Thank you for your patronage.")
                else:
                    print("Unable to tell if admin or user.")
                return str(login_details[4])
            else:
                print("Incorrect Password or Username.")
                user_failed = input("Try again or register? [0] to try once more, and [1] to register: ")
                if user_failed == "0":
                    textfile_reliant_login_function()
                elif user_failed == "1":
                    textfile_reliant_register_function()
                else:
                    print("Error. Invalid input.")
                    regis_or_log()

def textfile_reliant_register_function():
    # Take the user input for their data.
    admin_pass = str(input("To launch an admin account, enter the admin passcode: "))
    username = input("Enter the username you would like to use: ")
    password = input("Enter the password you would like to use: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
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
    if admin_pass == "eggs":
        login_file.write("1")
    else:
        login_file.write("0")
    login_file.close()
    print("User account creation success.")
    textfile_reliant_login_function()
