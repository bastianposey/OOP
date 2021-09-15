class phone:
    
    def __init__(self):
        self.__manufact = 0
        self.__model = ''
        self.__retail_price = 0

    def set_manufact(self,num):
        self.__manufact = num
    def set_model(self,mod):
        self.__model = mod
    def set_retail_price(self,price):
        self.__retail_price = price
    
    def get_manufact(self):
        return self.__manufact
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return self.__retail_price
    
