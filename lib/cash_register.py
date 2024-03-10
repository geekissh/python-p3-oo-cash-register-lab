#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.items = []
        self.total_price = 0
        self.last_transaction = 0

    def add_item(self, quantity, price):
        item_price = quantity * price
        self.items.append((quantity, price))
        self.total_price += item_price
        self.last_transaction = item_price
        return self.total_price

    def apply_discount(self, discount):
        total_price_float = float(self.total_price)
        discount_amount = total_price_float * (discount / 100)
        self.total_price -= int(discount_amount)
        self.last_transaction = -int(discount_amount)
        return self.total_price

    def void_last_transaction(self):
        last_transaction_amount = self.last_transaction
        self.total_price -= last_transaction_amount
        self.items.pop()
        if self.items:
            last_item_quantity, last_item_price = self.items[-1]
            self.last_transaction = last_item_quantity * last_item_price
        else:
            self.last_transaction = 0
        return self.total_price