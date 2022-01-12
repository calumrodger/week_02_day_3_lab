import unittest
from classes.customer import Customer
from classes.drink import Drink
from classes.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
        self.drink_1 = Drink("Heineken", 3, 1)
        self.drink_2 = Drink("Double Vodka", 5, 2)
        self.drink_3 = Drink("Irn-Bru", 1.5, 0)
        self.customer_1 = Customer("Andreas", 100, 31, True, 0)
        self.customer_2 = Customer("Calum", 50, 36, True, 0)
        self.customer_3 = Customer("Knox", 10, 2, True, 0)
        self.customer_4 = Customer("Rich", 500, 38, True, 10)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_customer_has_name(self):
        self.assertEqual("Andreas", self.customer_1.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink_1.price)

    def test_pub_can_add_drinks(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        self.pub.add_drink(self.drink_3)
        self.assertEqual(3, len(self.pub.drinks))

    def test_reduce_customer_cash(self):
        self.customer_1.reduce_cash(self.drink_1)
        self.assertEqual(97, self.customer_1.wallet)

    def test_increase_till_cash(self):
        self.pub.increase_till_cash(self.drink_1)
        self.assertEqual(1003, self.pub.till)

    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer(self.customer_1, self.drink_1)
        self.assertEqual(97, self.customer_1.wallet)
        self.assertEqual(1003, self.pub.till)
        self.assertEqual(1, self.customer_1.drunkenness)

    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer(self.customer_3, self.drink_1)
        self.assertEqual(10, self.customer_3.wallet)
        self.assertEqual(1000, self.pub.till)

    # def test_check_customer_age(self):
    #     self.customer_3.check_customer_age()
    #     self.assertEqual("not tonight", self.customer_3.check_customer_age())

    def test_check_customer_age(self):
        self.customer_3.check_customer_age()
        self.assertEqual(False, self.customer_3.okay_to_serve)

    def test_check_customer_age(self):
        self.customer_1.check_customer_age()
        self.assertEqual(True, self.customer_1.okay_to_serve)

    def test_check_customer_drunkenness(self):
        self.customer_1.check_customer_drunkenness()
        self.assertEqual(True, self.customer_1.okay_to_serve)

    def test_check_customer_drunkenness_2(self):
        self.customer_4.check_customer_drunkenness()
        self.customer_1.increase_drunkenness(self.drink_2)
        self.customer_1.increase_drunkenness(self.drink_2)
        self.customer_1.increase_drunkenness(self.drink_1)
        self.assertEqual(False, self.customer_4.okay_to_serve)



    def test_increase_drunkenness(self):
        self.customer_1.increase_drunkenness(self.drink_2)
        self.customer_1.increase_drunkenness(self.drink_2)
        self.customer_1.increase_drunkenness(self.drink_2)
        self.assertEqual(6, self.customer_1.drunkenness)
  
 