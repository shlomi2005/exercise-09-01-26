from classes.PaymentMethod import PaymentMethod


class PayPal(PaymentMethod):

    def pay(self, amount):
        return "Redirecting to PayPal " + str(amount)
