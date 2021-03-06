import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Beer", 5)

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink.drink_name)

    def test_drink_has_price(self):
        self.assertEqual(5, self.drink.price)