class Customer:

    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def reduce_cash(self, drink):
        self.wallet -= drink.price
        return self.wallet
    


