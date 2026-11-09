class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def subtotal(self):

        return sum(total["price"] * total["quantity"] for total in self.items)
