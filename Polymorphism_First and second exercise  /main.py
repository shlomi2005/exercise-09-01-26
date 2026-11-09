from classes.PaymentMethod import PaymentMethod
from classes.CreditCard import CreditCard
from classes.PayPal import PayPal
from classes.ApplePay import ApplePay


def checkout(method, amount):
    return f"{method.pay(amount)} | fee: {method.fee(amount)}"


for method in [CreditCard(), PayPal(), ApplePay()]:
    print(checkout(method, 100))
