import os
from lib.account import *
from lib.portfolio import *
from lib.market import *
from lib.tradealgo import *

version = 'IODO v0.1'

def displayMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(version)
    print('\n1) View Account Info')
    print('2) View Portfolio')
    print('3) View and Buy/Sell Shares')
    print('4) Start Trading Algorithm')
    print('5) Exit\n')
    return


def menu(account, api, conn, conn2):
    while True:
        try:
            userAction = int(input('What would you like to do?: '))
            if userAction == 1:
                displayMenu()
                accountInfo(account)
                menu(account, api, conn, conn2)
            elif userAction == 2:
                displayMenu()
                portfolio(api)
                menu(account, api, conn, conn2)
            elif userAction == 3:
                displayMarketMenu()
                marketMenu(account, api, conn, conn2)
            elif userAction == 4:
                ticker  = str(input('Enter the ticker you would like to trade or 0 to exit: '))
                if ticker == '0':
                    displayMenu()
                    menu(account, api, conn, conn2)
                else:
                    print('Initilizing...')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    #trade(api, ticker.upper(), capital)
                    trade = MartingaleTrader(api,conn2,ticker)
                    trade.start_trading()
                    #displayMenu()
                    #print('Trades have been logged and are available in /data/tradelogs-xxxxxxxx.txt')
                    #menu(account, api, conn, conn2)
            elif userAction == 5:
                print('Exiting...')
                break
            else:
                displayMenu()
                print('Invalid input\n')
                menu(account, api, conn)
        except ValueError:
            displayMenu()
            print('Invalid input\n')
            menu(account, api, conn)
        else:
            break
    return


def displayMarketMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(version)
    print('\n1) View Stock Info')
    print('2) View Current Buy/Sell Orders')
    print('3) Buy')
    print('4) Sell')
    print('5) Return\n')

    return


def marketMenu(account, api, conn, conn2):
    clock = api.get_clock()
    print('The market is {}'.format('open.\n' if clock.is_open else 'closed.\nOrders can still be placed however they will be executed when the market is next open.\n'))
    while True:
        try:
            userAction = int(input('What would you like to do?: '))
            if userAction == 1:
                tickers  = str(input('Enter the ticker(s) you would like to view or 0 to exit\nYou can enter more than one symbol by separating them with a space.: '))
                if tickers == '0':
                    displayMarketMenu()
                    marketMenu(account, api, conn, conn2)
                else:
                    displayMarketMenu()
                    viewStock(api, tickers.upper())
                    marketMenu(account, api, conn, conn2)
            elif userAction == 2:
                displayMarketMenu()
                viewOrders(conn, api)
                marketMenu(account, api, conn, conn2)
            elif userAction == 3:
                ticker = str(input('Enter the ticker of the stock you would like to buy or 0 to exit: '))
                if ticker == '0':
                    displayMarketMenu()
                    marketMenu(account, api, conn, conn2)
                else:
                    displayMarketMenu()
                    buyShares(api, ticker.upper())
                    marketMenu(account, api, conn, conn2)
            elif userAction == 4:
                displayMarketMenu()
                portfolio(api)
                ticker = str(input('Enter the ticker of the stock you would like to sell or 0 to exit: '))
                if ticker == '0':
                    displayMarketMenu()
                    marketMenu(account, api, conn, conn2)
                else:
                    displayMarketMenu()
                    sellShares(api, ticker.upper())
                    marketMenu(account, api, conn, conn2)
            elif userAction == 5:
                displayMenu()
                menu(account, api, conn, conn2)
            else:
                displayMarketMenu()
                print('Invalid input\n')
                marketMenu(account, api, conn, conn2)
        except ValueError:
            displayMarketMenu()
            print('Invalid input\n')
            marketMenu(account, api, conn, conn2)
        else:
            break   
    return 