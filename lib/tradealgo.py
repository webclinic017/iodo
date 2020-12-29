class Portfolio:

    def __init__(self, capital, shares):
        self.capital = capital
        self.shares = shares
        self.total_value = self.capital + self.shares


def trade(api, ticker, amount):
    return