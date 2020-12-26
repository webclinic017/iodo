#!/usr/bin/env python3

#IODO
#v0.1
#A simple stock market application and trading algorithm using the Alpaca API
#Gavin Su me@gavin.su

import os
import alpaca_trade_api as tradeAPI
from readWriteAPI import *

version = 'IODO v0.1'

def accountInfo(account):
    if account.trading_blocked:
        print('Account is restricted from trading.')
    print('Account equity:', float(account.equity))
    print('Buying power:', float(account.buying_power))
    print('Portfolio value:', float(account.portfolio_value), '\n')
    return


def displayMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(version)
    print('\n1) View Account Info')
    print('2) View Portfolio')
    print('3) Buy or Sell Shares')
    print('4) Initiate Trading')
    print('5) Exit\n')
    return


def portfolio(account):
    try:
        portfolio = account.list_positions()
        for position in portfolio:
            print('{}   | {}    | {}    | {}    | {}    | {}', 
                    position.symbol, 
                    position.qty,
                    position.market_value,
                    position.unrealized_plpc,
                    position.current_price, 
                    position.change_today)
        print('\n')
    except AttributeError:
        print('You have no positions currently.\n')
    return


def displayMarketMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(version)
    print('\n1) View Stock Info')
    print('2) Buy')
    print('3) Sell')
    print('4) Return\n')
    return


def marketMenu(account):
    while True:
        try:
            userAction = int(input('What would you like to do?: '))
            if userAction == 1:
                symbol = str(input('Please enter the symbol you would like to view or 0 to exit: '))
                if symbol == '0':
                    displayMarketMenu()
                    marketMenu(account)
                else:
                    displayMarketMenu()
                    viewStock(account, symbol)
                    marketMenu(account)
            elif userAction == 2:
                displayMarketMenu()
                pass
                marketMenu(account)
            elif userAction == 3:
                displayMarketMenu()
                pass
                marketMenu(account)
            elif userAction == 4:
                displayMenu()
                menu(account)
            else:
                displayMarketMenu()
                print('Invalid input\n')
                marketMenu(account)
        except ValueError:
            displayMarketMenu()
            print('Invalid input\n')
            marketMenu(account)
        else:
            break   
    return 


def viewStock(account, symbol):

    return


def menu(account):
    while True:
        try:
            userAction = int(input('What would you like to do?: '))
            if userAction == 1:
                displayMenu()
                accountInfo(account)       
                menu(account)
            elif userAction == 2:
                displayMenu()
                portfolio(account)
                menu(account)
            elif userAction == 3:
                displayMarketMenu()
                marketMenu(account)
            elif userAction == 5:
                break
            else:
                displayMenu()
                print('Invalid input\n')
                menu(account)
        except ValueError:
            displayMenu()
            print('Invalid input\n')
            menu(account)
        else:
            break
    return


def main():
    #APCA_API_KEY_ID = 'PKTLIY1IA0Z9SIQV3CDB'
    #APCA_API_SECRET_KEY = 'zvJn3SK86gF8SeI00nQfZmuTSKoMbwi25lWu8xv1'
    APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
    APCA_API_KEY_ID = loadAPIKey()
    APCA_API_SECRET_KEY = loadSecretKey()

    if APCA_API_KEY_ID == 'Not Set':
        APCA_API_KEY_ID = str(input('Please enter your API key: '))
        APCA_API_SECRET_KEY = str(input('Please enter your secret key: '))
        writeAPIKey(APCA_API_KEY_ID, APCA_API_SECRET_KEY)
    else:
        while True:
            apiAccount = str(input('Would you like to enter a new API key? (y/n): '))
            if apiAccount == 'y' or apiAccount == 'Y':
                APCA_API_KEY_ID = str(input('Please enter your API key: '))
                APCA_API_SECRET_KEY = str(input('Please enter your secret key: '))
                writeAPIKey(APCA_API_KEY_ID, APCA_API_SECRET_KEY)
            elif apiAccount == 'n' or apiAccount == 'N':
                break
            else:
                print('Please enter a valid option.')

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Validating...')
    api = tradeAPI.REST(APCA_API_KEY_ID, 
            APCA_API_SECRET_KEY, 
            APCA_API_BASE_URL)
    account = api.get_account()
    os.system('cls' if os.name == 'nt' else 'clear')
    displayMenu()
    menu(account)
    return


if __name__ == '__main__':
    main()
