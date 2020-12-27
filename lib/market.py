import os

def viewStock(api, tickers):
    tickerList = sorted(tickers.split())
    for ticker in tickerList:
        price = api.get_last_quote(ticker)
        print('{}\t| Asking: ${}\t| Bidding: ${}'.format(
            ticker, 
            price.askprice, 
            price.bidprice))
    print('\n')
    return


def buyShares(api, ticker):
    viewStock(api, ticker)
    amount = int(input('Enter the amount of shares you would like to buy or 0 to exit: '))
    if amount == 0:
        return
    else:
        api.submit_order(
            symbol=ticker,
            qty=amount,
            side='buy',
            type='market',
            time_in_force='gtc')
        print('Buy order submitted succesfully.\n')
    return


def sellShares(api, ticker):
    viewStock(api, ticker)
    amount = int(input('Enter the amount of shares you would like to sell or 0 to exit: '))
    if amount == 0:
        return
    else:
        api.submit_order(
            symbol=ticker,
            qty=amount,
            side='sell',
            type='market',
            time_in_force='gtc')
        print('Sell order submitted succesfully.\n')
    return