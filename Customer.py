class Customer:
    def __init__(self, first_name, last_name):
        self.__full_name = first_name
        self.__last_name = last_name
        
    def get_first_name(self):
        return self.__full_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_account(self):
        return self.__account
    
    def set_account(self, account):
        self.__account = account
