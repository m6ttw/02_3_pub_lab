class Pub():
    
    def __init__(self, pub_name, till, drinks):
        self.pub_name = pub_name
        self.till = till
        self.drinks = drinks
        self.drinks_sold = 0

    def increase_till(self, drink):
        self.till += drink.price

    # def sell_drink_to_customer(self, drink_name, customer):
    #     drink = self.find_pet_by