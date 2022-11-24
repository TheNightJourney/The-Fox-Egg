from Customer import Customer
class Bank:
    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__customer_count = 0
        self.__customers = list()
        
    def add_customer(self, first_name, last_name):
        self.__customers.append(Customer(first_name, last_name))
        self.__customer_count += 1
        
    def get_customer_count(self):
        return self.__customer_count
    
    def get_customer(self, index):
        return self.__customers[index]
    
    
        
        
    