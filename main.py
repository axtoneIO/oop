from pkgutil import iter_modules
from random import random


class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity: float): #Parametro opcional quantity
        print(f"An instance created {name}")
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        # Assign to self object
        self.name       = name
        self.price      = price
        self.quantity   = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_disccount(self):
        self.price = self.price * Item.pay_rate

    # class method
    @classmethod
    def instantiate_from_csv(self):
        pass

    # tostring common method
    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"


    # calling a class method from the class level only
    Item.instantiate_from_csv()
