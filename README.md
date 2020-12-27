# iodo
An attempt to create an algorithm to succesfully trade stocks on the US stock market.

This uses the API provided by https://alpaca.markets/


You will need to create an account to get your API and secret key.
Create a file named apiKey.json with {"API_Key": "Not Set", "Secret_Key": "Not Set"} inside and place it in /data/key.
Run the iodo.py file.


# todo
* finish writing up the functions to view and buy/sell shares.
* write the algorithm for trading.
* get price streaming through websockets working | Note: Looks like its only available on polygon which is US residents only :(
* extending functionality such as limit orders
* ability look at historical data

# working
* account info
* viewing portfolio
* viewing stock asking and bidding prices (not sure if im using correct endpoint for this)
* buying shares
