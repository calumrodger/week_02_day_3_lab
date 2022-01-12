import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.pub_2 = Pub("The Watering Hole", 1000)
        self.drink = Drink("Heineken", 3, 1)
        self.drink_1 = Drink("Double Vodka", 5, 2)
        self.drink_2 = Drink("Irn-Bru", 1.5, 0)
        self.customer = Customer("Andreas", 100, 31, 0)
        self.customer_1 = Customer("Calum", 50, 36, 0)
        self.customer_2 = Customer("Knox", 10, 2, 0)
    
    def test_pub_has_name(self):
        self.assertEqual("The Watering Hole", self.pub_2.name)

    def test_customer_has_name(self):
        self.assertEqual("Andreas", self.customer.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)
    
    def test_pub_has_drink_collection(self):
        self.assertEqual(1, len(self.pub.drinks))

    def test_reduce_customer_cash(self):
        self.customer.reduce_cash(self.drink)
        self.assertEqual(97, self.customer.wallet)

    def test_increase_till_cash(self):
        self.pub.increase_till_cash(self.drink)
        self.assertEqual(1003, self.pub.till)

    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer(self.customer, self.drink)
        self.assertEqual(97, self.customer.wallet)
        self.assertEqual(1003, self.pub.till)