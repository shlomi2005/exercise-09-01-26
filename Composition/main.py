from classes.Cart import Cart
from classes.Checkout import Checkout
from classes.IsraeliVat import IsraeliVat
from classes.TaxExempt import TaxExempt


cart = Cart()
cart.add("Pen", 5, 4)
cart.add("Bag", 60)
checkout1 = Checkout(cart, IsraeliVat())
checkout2 = Checkout(cart, TaxExempt())
for checkout in [checkout1, checkout2]:
    print(checkout.total())
