import requests

spx_ticker = "SPX"
dow_ticker = "DOW"
api_key = "9f97c07bdd4c4646b36f44e939057ed5"


def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


stockdata_spx = get_stock_quote(spx_ticker, api_key)
stock_price_spx = get_stock_price(spx_ticker, api_key)
stockdata_dow = get_stock_quote(dow_ticker, api_key)
stock_price_dow = get_stock_price(dow_ticker, api_key)


percentChange_spx = float(stockdata_spx['percent_change'])
percentChange_dow = float(stockdata_dow['percent_change'])


print(percentChange_dow, "%", "-Dow Jones Industrial Average")
print(percentChange_spx, "%", "-S&P 500 percent change")

market_rep = round((percentChange_dow / percentChange_spx))
print(market_rep, "Today's market")


print(stock_price_spx)
print(stock_price_dow)

def getMood(percent, lower,upper ):
    print(percent)
    if percent > upper:
        print("Serotonin is high")
    if percent < lower:
         print("Serotonin is low")
    return

getMood(market_rep, 0.5, 1.5)
#i = 0
# while i <= 10:
#    print(name, "$", stock_price)

#print(name, "$", stock_price)
#print("Exchange = ", exchange)
#print("Currency = ", currency)
#print("Open price = ", "$", open_price)
#print("high price = ", "$", high_price)
#print("low price = ", "$", low_price)
#print("close price = ", "$", close_price)
#print("Volume traded = ", "USD$", volume)

#exchange = stockdata['exchange']
#currency = stockdata['currency']
#open_price = stockdata['open']
#high_price = stockdata['high']
#low_price = stockdata['low']
#close_price = stockdata['close']
#volume = stockdata['volume']
#name = stockdata['name']
