class Portfolio:

    def __init__(self, capital, price):
        self.capital = capital
        self.price = price
        self.shares = self.capital % self.price
        #self.total_value = self.capital + self.shares


def trade(api, ticker, amount):
    return