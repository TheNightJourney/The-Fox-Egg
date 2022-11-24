from Account import Account
from Bank import Bank


def main():
    b1 = Bank("BCA")
    
    # adding a customer to the bank
    b1.add_customer("Kimi", "Elliptic")
    b1.add_customer("Ore", "Tamago")
    b1.add_customer("Ano", "Egg")
    
    # getting the total number of customers
    print(b1.get_customer_count())
    
    # accessing info of a customer
    print(b1.get_customer(2).get_first_name())
    print(b1.get_customer(2).get_last_name())
    
    # create an account for a customer
    b1.get_customer(2).set_account(Account(500000))
    
    print(b1.get_customer(2).get_account().get_balance())
    
    if b1.get_customer(2).get_account().deposit(1000000):
        print(b1.get_customer(2).get_account().get_balance())
    else:
        print("Invalid")
        
    
if __name__ == "__main__":
    main()
