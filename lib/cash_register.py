class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, item_name, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        for _ in range(quantity):
            self.items.append(item_name)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_item_cost = self.items.pop()  # Remove the last item from the list.
            self.total -= last_item_cost