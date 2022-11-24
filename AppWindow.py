from register_or_login import *
from Customer_Page import *


# Entry text.
entry_function()

# To register or log in (the register loops to log in once finished).
user = regis_or_log()
print("\n")

if user == "1":
    print("Admin panel under construction.")
elif user == "0":
    customer_menu_panel()
else:
    print("Unknown user detected.", type(user), user)

