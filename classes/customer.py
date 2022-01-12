class Customer:

    def __init__(self, name, wallet, age, drunkenness, fav_drink):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness
        self.fav_drink = fav_drink

    def reduce_cash(self, drink):
        self.wallet -= drink.price
        return self.wallet
    
    


    # def increase_drunken_level

    # def increase_till_cash

    # def customer_buys_drink(self, till, wallet, price):

