def portfolio(account):
    try:
        portfolio = account.list_positions()
        for position in portfolio:
            print('{}\t| {}\t| {}\t| {}\t| {}\t| {}'.format( 
                    position.symbol, 
                    position.qty,
                    position.market_value,
                    position.unrealized_plpc,
                    position.current_price, 
                    position.change_today))
        print('\n')
    except AttributeError:
        print('You have no positions currently.\n')
    return