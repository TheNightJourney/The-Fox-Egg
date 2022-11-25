from register_or_login import *
from Customer_Page import *
import os


# Clear previous statements.
os.system('cls')

# Entry text.
entry_function()

# To register or log in (the register loops to log in once finished).
user = regis_or_log()

# Decision to open the admin panel or user panel.
for line in open('admin_information.txt', 'r').readlines():
    find_admin = line.split(";")
    if user == find_admin[0]:
        print("Admin panel under construction.")
    else:
        for other_line in open('customer_login_information.txt', 'r'):
            find_customer = other_line.split(";")
            if user != find_customer[0]:
                continue
            else:
                print("\nCustomer menu loading...\n")
                customer_menu_panel(user)
