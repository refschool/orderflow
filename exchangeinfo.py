import binancelib as b
tickers = b.get_exchange_info()
tickers.sort()
print(tickers)