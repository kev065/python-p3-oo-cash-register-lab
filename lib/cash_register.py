#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0): # Initializes the class with default parameters for discount, total and items
      self.discount = discount 
      self.total = 0 # sets the discount rate
      self.items = [] # initializes the list of items

    def add_item(self, title, price, quantity = 1): # defines a method to add an item to the cart
      self.cart = price * quantity # calculates the cost based on quantity of items
      self.total += self.cart # adds the cost to the total
      for i in range(quantity): # for each item in the quantity
        self.items.append(title) # add the item to the list of items
    
    def apply_discount(self): # defines a method to apply a discount to the total cost
      if self.discount > 0: # if there is a discount,
        discount_percent = (100 - self.discount) / 100 # calculate the discount percentage
        self.total = int(self.total * discount_percent) # apply the discount to the total cost
        print(f'After the discount, the total comes to ${self.total}.') # prints the discounted total cost
      else: # if there is no discount, 
        print('There is no discount to apply.') # print the message 'There is no discount to apply.'
    
    def void_last_transaction(self): # defines a method to void the last transaction
      self.total -= self.cart # substracts the cost of the last item from the total