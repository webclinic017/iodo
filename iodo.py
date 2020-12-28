#!/usr/bin/env python3

#IODO
#v0.1
#A simple stock market application and trading algorithm using the Alpaca API
#Gavin Su me@gavin.su

import os
import alpaca_trade_api as tradeAPI
from lib.rwKeys import *
from lib.account import *
from lib.menu import *
from lib.portfolio import *
from lib.market import *


def main():
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
    conn = tradeAPI.StreamConn(APCA_API_KEY_ID,
            APCA_API_SECRET_KEY,
            APCA_API_BASE_URL)
    account = api.get_account()
    os.system('cls' if os.name == 'nt' else 'clear')
    displayMenu()
    menu(account, api, conn)
    return


if __name__ == '__main__':
    main()
