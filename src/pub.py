class Pub():
    
    def __init__(self, pub_name, till, drinks):
        self.pub_name = pub_name
        self.till = till
        self.drinks = drinks
        self.drinks_sold = 0
        self.customers = []

    def increase_till(self, drink):
        if customer.age >= 18:
            self.till += drink.price

    def sell_drink_to_customer(self, drink):
        if customer.age >= 18:
            self.drinks_sold += 1