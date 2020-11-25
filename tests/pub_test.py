import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink_name_1 = Drink("Beer", 5)
        self.drink_name_2 = Drink("Ale", 4)
        self.drink_name_3 = Drink("Mead", 6)

        drinks = [self.drink_name_1, self.drink_name_2, self.drink_name_3]
        self.pub = Pub("The Prancing Pony", 100, drinks)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.pub_name)

    def test_pub_has_money(self):
        self.assertEqual(100, self.pub.till)

    def test_can_increase_till(self):
        self.pub.increase_till(self.drink_name_1)
        self.assertEqual(105, self.pub.till)

    def test_can_sell_drink(self):
        self.pub.sell_drink_to_customer(self.drink_name_1)
        self.assertEqual(1, self.pub.drinks_sold)