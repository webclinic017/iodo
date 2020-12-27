import os
from lib.account import *
from lib.portfolio import *
from lib.market import *

version = 'IODO v0.1'

def displayMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(version)
    print('\n1) View Account Info')
    print('2) View Portfolio')
    print('3) View and Buy/Sell Shares')
    print('4) Initiate Algorithmic Trading')
    print('5) Exit\n')
    return


def menu(account, api):
    while True:
        try:
            userAction = int(input('What would you like to do?: '))
            if userAction == 1:
                displayMenu()
                accountInfo(account)
                menu(account, api)
            elif userAction == 2:
                displayMenu()
                portfolio(account)
                menu(account, api)
            elif userAction == 3:
                displayMarketMenu()
                marketMenu(account, api)
            elif userAction == 5:
                break
            else:
                displayMenu()
                print('Invalid input\n')
                menu(account, api)
        except ValueError:
            displayMenu()
            print('Invalid input\n')
            menu(account, api)
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


def marketMenu(account, api):
    clock = api.get_clock()
    print('The market is {}'.format('open.\n' if clock.is_open else 'closed.\nOrders can still be placed however they will be executed when the market is next open.\n'))
    while True:
        try:
            userAction = int(input('What would you like to do?: '))
            if userAction == 1:
                tickers  = str(input('Enter the ticker(s) you would like to view or 0 to exit\nYou can enter more than one symbol by separating them with a space.: '))
                if tickers == '0':
                    displayMarketMenu()
                    marketMenu(account, api)
                else:
                    displayMarketMenu()
                    viewStock(api, tickers.upper())
                    marketMenu(account, api)
            elif userAction == 2:
                displayMarketMenu()
                marketMenu(account, api)
            elif userAction == 3:
                ticker = str(input('Enter the ticker of the stock you would like to buy or 0 to exit: '))
                if ticker == '0':
                    displayMarketMenu()
                    marketMenu(account, api)
                else:
                    displayMarketMenu()
                    buyShares(api, ticker.upper())
                    marketMenu(account, api)
            elif userAction == 4:
                displayMarketMenu()
                portfolio(account)
                ticker = str(input('Enter the ticker of the stock you would like to sell or 0 to exit: '))
                if ticker == '0':
                    displayMarketMenu()
                    marketMenu(account, api)
                else:
                    displayMarketMenu()
                    sellShares(api, ticker.upper())
                    marketMenu(account, api)
            elif userAction == 5:
                displayMenu()
                menu(account, api)
            else:
                displayMarketMenu()
                print('Invalid input\n')
                marketMenu(account, api)
        except ValueError:
            displayMarketMenu()
            print('Invalid input\n')
            marketMenu(account, api)
        else:
            break   
    return 