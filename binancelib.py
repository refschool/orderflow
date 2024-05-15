import requests

def get_chart(symbols,timeframe='30m',limit=10):
    chart = []
    for symbol in symbols:
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={timeframe}&limit={limit}"
        print(url)
        r = requests.get(f'{url}')
        ticker_object  = {'symbol':symbol,'candles':r.json()}
        chart.append(ticker_object)
    return chart

def is_green(candle):
   # print(candle)
    open = candle[1]
    close = candle[4]

    """ compare close to open"""
    delta = float(close) - float(open)
    if(delta > 0):

        return True
    return False


def is_streak(ticker_object):
    """ find 3 consecutive green candles """
    symbol = ticker_object['symbol']
    candles = ticker_object['candles']
    print(f"computing for {symbol}")
    streak = []
    for candle in candles[-3:]:
        if is_green(candle):
            streak.append(candle)
    if len(streak) == 3:
        print("TRUE")
        return True
    return False


def is_big_green_candle(candles,times_to_average = 5):
    import statistics
    filtered_candles = []
    """ remove last candle """
    last_candle = candles.pop(-1)
    """ detect if last candle is bigger than average candle size """
    average_green_candle_body_size = 0
    for candle in candles:
        if is_green(candle):
            filtered_candles.append(candle)





def get_exchange_info():
    url = f"https://api.binance.com/api/v3/exchangeInfo"
    r = requests.get(url)
    symbols = r.json()['symbols']
    ticker = []
    for s in symbols:
        ticker.append(s['symbol'])
    return ticker

def get_order_book(symbol="BTCUSDT",limit=10):
    url = f"https://api.binance.com/api/v3/depth"
    r = requests.get(url,"symbol={}&limit={}".format(symbol,limit))
    result = r.json()
    return result