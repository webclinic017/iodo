# iodo
An attempt to create an algorithm to succesfully trade stocks on the US stock market.

This uses the API provided by https://alpaca.markets/
and the API wrapper provided by Alpaca markets. https://github.com/alpacahq/alpaca-trade-api-python

Additional libraries required if not already installed are:
`dateutil`
`numpy`
`pandas`
`pytz`
`websockets`

##### How to use
1. You will need to create an account to get your API and secret key by visiting https://alpaca.markets/

2. Create a file named apiKey.json with
    `{"API_Key": "Not Set", "Secret_Key": "Not Set"}`
and place it in /data/key.
An example json file is placed in there (Just remove the .backup extension).
You can add your API and secret key there if you don't want to add it within the program.

3. Run `iodo.py` to start.


### To do list
* finish writing up the functions to view and buy/sell shares.
* write the algorithm for trading.
* ~~get price streaming through websockets working~~ Looks like its only available on polygon which is US residents only :(
* extending functionality such as limit orders
* ability look at historical data

### Working
* account info
* viewing portfolio
* viewing stock asking and bidding prices (not sure if im using correct endpoint for this)
* buying shares
