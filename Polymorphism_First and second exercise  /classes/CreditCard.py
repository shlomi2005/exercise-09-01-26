from classes.PaymentMethod import PaymentMethod


class CreditCard(PaymentMethod):

    def pay(self, amount):
        return "Charging card " + str(amount)

    def fee(self, amount):
        return 2
