def accountInfo(account):
    if account.trading_blocked:
        print('Account is restricted from trading.')
    print('Account equity:', float(account.equity))
    print('Buying power:', float(account.buying_power))
    print('Portfolio value:', float(account.portfolio_value), '\n')
    return