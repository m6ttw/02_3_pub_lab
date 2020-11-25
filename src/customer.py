class Customer():

    def __init__(self, customer_name, wallet):
        self.customer_name = customer_name
        self.wallet = wallet

    def decrease_wallet(self, amount):
        self.wallet -= amount