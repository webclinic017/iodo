import os
import time
import datetime
import threading
import multiprocessing

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


def viewOrders(conn, api):
    orders = api.list_orders()
    for order in orders:
        print('{}\t| Quantity: {}\t| Buy/Sell: {}'.format(order.symbol, order.qty, order.side))
    print('\n')
    #t1 = threading.Thread(target = streamOrders(conn))
    #t2 = threading.Thread(target = endStream(conn))
    #t1 = multiprocessing.Process(target = streamOrders(conn))
    #t2 = multiprocessing.Process(target = endStream(conn))
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()
    
    return


def streamOrders(conn):
    @conn.on(r'trade_updates')
    async def on_msg(conn, data, symbol):
        symbol = data.order['symbol']
        event = data.event
        print('Order executed for', symbol, data.order['side'], event, data.order['filled_qty'])
    conn.run(['trade_updates'])
    return


def endStream(conn):
    print('test3')
    time.sleep(0.2)
    userAction = int(input('Press 0 to stop streaming: '))
    if userAction == 0:
        conn.close()
        return