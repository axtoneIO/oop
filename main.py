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

# tostring common method
    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Phone",100,1)

# item1.apply_disccount()
# print(item1.price)

# item2 = Item("Laptop",50,5)

# item2.price = 1000
# item2.quantity = 3

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.__dict__) # All tha attributes for class level
# print(item1.__dict__) # All the attributes for instance level

item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)

# for instance in Item.all:
#     print(instance.name)

print(Item.all)