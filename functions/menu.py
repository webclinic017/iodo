import os
from functions.account import *
from functions.portfolio import *
from functions.market import *

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
    print('2) Buy')
    print('3) Sell')
    print('4) Return\n')
    return


def marketMenu(account, api):
    while True:
        try:
            userAction = int(input('What would you like to do?: '))
            if userAction == 1:
                symbols  = str(input('Please enter the symbol(s) you would like to view or 0 to exit\n(You can enter more than one symbol by separating them with a space.): '))
                if symbols == '0':
                    displayMarketMenu()
                    marketMenu(account, api)
                else:
                    displayMarketMenu()
                    viewStock(api, symbols.upper())
                    marketMenu(account, api)
            elif userAction == 2:
                displayMarketMenu()
                pass
                marketMenu(account, api)
            elif userAction == 3:
                displayMarketMenu()
                pass
                marketMenu(account, api)
            elif userAction == 4:
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