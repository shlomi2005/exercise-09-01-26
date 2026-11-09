from classes.Cart import Cart


class Checkout:
    def __init__(self, cart, vat):
        self.cart = cart
        self.vat = vat

    def total(self):
        return self.vat.apply(self.cart.subtotal())
