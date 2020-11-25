# A Customer should be able to buy a Drink from the Pub,
# reducing the money in its wallet
# and increasing the money in the Pub's till

import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Frodo Baggins", 100)

    def test_customer_has_name(self):
        self.assertEqual("Frodo Baggins", self.customer.customer_name)

    def test_customer_has_money(self):
        self.assertEqual(100, self.customer.wallet)

    def test_can_decrease_wallet(self):
        self.customer.decrease_wallet(5)
        self.assertEqual(95, self.customer.wallet)
    