class Customer:

    def __init__(self, name, wallet, age, okay_to_serve, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.okay_to_serve = okay_to_serve
        self.drunkenness = drunkenness

    def reduce_cash(self, drink):
        self.wallet -= drink.price
        return self.wallet

    def remove_customer(self):
        self.remove(self)

    # def check_customer_age(self):
    #     if self.age < 19:
    #         return "not tonight"

    def check_customer_age(self):
        if self.age < 19:
            self.okay_to_serve = False

    def check_customer_drunkenness(self):
        if self.drunkenness > 4:
            self.okay_to_serve = False

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level


