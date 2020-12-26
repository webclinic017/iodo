import os

def viewStock(api, symbols):
    symbolList = sorted(symbols.split())
    for symbol in symbolList:
        price = api.get_last_quote(symbol)
        print('{}\t| Asking: ${}\t| Bidding: ${}'.format(
            symbol, 
            price.askprice, 
            price.bidprice))
    print('\n')
    return