class Customer():

    def __init__(self, customer_name, wallet):
        self.customer_name = customer_name
        self.wallet = wallet
        self.stomach = []

    def decrease_wallet(self, drink):
        self.wallet -= drink.price

    def buy_drink_from_pub(self, drink):
        self.stomach.append(drink)