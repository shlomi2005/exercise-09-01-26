from classes.PaymentMethod import PaymentMethod


class ApplePay(PaymentMethod):

    def pay(self, amount):
        return "Paid with Apple Pay" + str(amount)
