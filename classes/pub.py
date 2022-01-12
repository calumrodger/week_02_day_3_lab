class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drinks_to_menu(self, drink):
        self.append(drink)
        print(drink)


    def increase_till_cash(self, drink):
        self.till += drink.price


    def sell_drink_to_customer(self, customer, drink):
        customer.reduce_cash(drink)
        self.increase_till_cash(drink)
    