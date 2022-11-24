import pandas as np
import pandas as pd


def register_or_login():
    initial_input = int(input("\n[0] or [1]: "))
    if initial_input == 0:
        return pandas_register_function()
    elif initial_input == 1:
        return pandas_login_function()
    else:
        return "Input error. Please try again."


def pandas_login_function():
    df_login_info = pd.read_csv('login_information.csv')
    # Code visualisation: Enter the username and password.
    username = input("Enter your username: ")
    password = input("Enter your password: ")






pandas_login_function()