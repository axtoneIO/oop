from ast import Try
import csv
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
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    # tostring common method
    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(7.5))
