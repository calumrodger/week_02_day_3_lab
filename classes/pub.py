class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    # def add_drinks_to_menu(self, drink):
    #     self.append(drink)
    #     print(drink)


    def increase_till_cash(self, drink):
        self.till += drink.price

    def add_drink(self, drink):
        self.drinks.append(drink)
  

    def pub_has_drink_collection(self):
        return len(self.drinks)


    def sell_drink_to_customer(self, customer, drink):
        customer.reduce_cash(drink)
        self.increase_till_cash(drink)

    def check_customer_age(self, customer):
        if customer.age < 19:
            return False
    