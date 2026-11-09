class PaymentMethod:
    def pay(self):
        raise ValueError("NotImplementedError")

    def fee(self, amount):
        return 0
