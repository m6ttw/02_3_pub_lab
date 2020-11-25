class Customer():

    def __init__(self, customer_name, wallet, age):
        self.customer_name = customer_name
        self.wallet = wallet
        self.stomach = []
        self.age = age

    def decrease_wallet(self, drink):
        if self.age >= 18:
            self.wallet -= drink.price

    def buy_drink_from_pub(self, drink):
        if self.age >= 18:
            self.stomach.append(drink)