class Customer():

    def __init__(self, customer_name, wallet):
        self.customer_name = customer_name
        self.wallet = wallet

    def decrease_wallet(self, drink):
        self.wallet -= drink.price