#https://binance-docs.github.io/apidocs/spot/en/#introduction
#OHLC
APIKEY = "oRFkPNCpZGrmLywS93oQPpdJzY3p3t3hlr8sSRKZJ9HUmo57dniMEaWpvmWF7VeI"
symbols = ['LRCUSDT','DOTUSDT','BTCUSDT','ETHUSDT','VETUSDT','AVAXUSDT','LUNAUSDT','LINKUSDT',
           'SOLUSDT','MATICUSDT','ADAUSDT','AAVEUSDT','CAKEUSDT','UNIUSDT','ENJUSDT','EGLDUSDT',
           'CHZUSDT','TRXUSDT','ONEUSDT','XTZUSDT','SXPUSDT','TFUELUSDT','THETAUSDT',
           'LRCUSDT','XMRUSDT','FILUSDT','MDXUSDT','FTMUSDT','XLMUSDT',
           'ICPUSDT','ETCUSDT','EOSUSDT','FTTUSDT','GRTUSDT','ATOMUSDT','NEOUSDT','AXSUSDT',
            'FLOWUSDT','COMPUSDT','SUSHIUSDT','HNTUSDT','ZRXUSDT',
           'KSMUSDT','STXUSDT','XEMUSDT','WAVESUSDT','RVNUSDT','BATUSDT','ALGOUSDT','NEARUSDT','ZILUSDT',
           'ONTUSDT','OMGUSDT','ZECUSDT','QTUMUSDT','HBARUSDT','SNXUSDT','ICXUSDT','ARUSDT','MANAUSDT']

#symbols = ['FUNUSDT']

import binancelib as b
import time

chart = b.get_chart(symbols)
for ticker in chart:
    if b.is_streak(ticker):
        print('True')

time.sleep(4)

chart = b.get_chart(symbols,timeframe='1h')
for ticker in chart:
    if b.is_streak(ticker):
        print('True')
