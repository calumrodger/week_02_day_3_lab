class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []


    def increase_till_cash(self, drink):
        self.till += drink.price

    def add_drink(self, drink):
        self.drinks.append(drink)
  

    def pub_has_drink_collection(self):
        return len(self.drinks)


    def sell_drink_to_customer(self, customer, drink):
        customer.check_customer_age()
        if customer.okay_to_serve == True:
            customer.reduce_cash(drink)
            customer.increase_drunkenness(drink)
            self.increase_till_cash(drink)
        else: 
            return("no service")


    