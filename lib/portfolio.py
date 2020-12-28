def portfolio(api):
    #try:
    portfolio = api.list_positions()
    #portfolio.sort()
    for position in portfolio:
        print('{}\t| {}\t| ${}\t| ${}\t| {}%\t| {}%'.format( 
                position.symbol, 
                position.qty,
                float(position.market_value),
                float(position.current_price),
                round(float(position.unrealized_plpc), 2),
                round(float(position.change_today), 2)
                ))
    print('\n')
    #except AttributeError:
    #    print('You have no positions currently.\n')
    return