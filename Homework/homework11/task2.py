"""
You are given the following code.

class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
import types


class Order:
    def __init__(self, price, discount_price=None):
        self.price = price
        if discount_price:
            self.discount_price = types.MethodType(discount_price, self)

    def final_price(self):
        try:
            return self.discount_price()
        except AttributeError:
            return self.price
