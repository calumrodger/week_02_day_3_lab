import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.drink = Drink("Heineken", 3, 1)
        self.drink_2 = Drink("Double Vodka", 5, 2)
        self.drink_3 = Drink("Irn-Bru", 1.5, 0)
        self.customer = Customer("Andreas", 100, 31, 0)
        self.customer_2 = Customer("Calum", 50, 36, 0)
        self.customer_3 = Customer("Knox", 10, 2, 0)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_customer_has_name(self):
        self.assertEqual("Andreas", self.customer.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)

    # def test_can_add_drinks_to_menu(self):
    #     self.pub.add_drinks_to_menu(self.drink)
    #     self.assertEqual(3, self.pub.drinks())

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

    # def test_check_customer_age(self):
    #     self.pub.check_customer_age(self.customer)
    #     self.assertEqual(False, self.customer.age)

    def test_pub_can_add_drinks(self):
        self.pub.add_drink(self.drink)
        self.pub.add_drink(self.drink_2)
        self.pub.add_drink(self.drink_3)
        self.assertEqual(3, len(self.pub.drinks))
 