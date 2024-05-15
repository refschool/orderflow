#https://binance-docs.github.io/apidocs/spot/en/#change-log
# see doc >> https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md
# https://stackoverflow.com/questions/21236824/unresolved-reference-issue-in-pycharm
import requests
import pandas as pd
import pprint
import json
import numpy as np
from mail_lib import send_mail
import math
from cryptosymbols import symbols,timeframes

from bblib import get_klines,get_bollinger,build_endpoint,process_bb_overbought_logic,process_bb_oversold_logic
import time
""" construction endpoint """

while True:
    """ designed to continuously run but okay for 4H and daily no need"""
    for timeframe in timeframes:
        """ for loop  """
        for symbol in symbols:
            print(f"processing {symbol} for {timeframe} ")

            url = build_endpoint(symbol,timeframe,100)
            candles = get_klines(url)
            symbol_df = get_bollinger(candles)

            #extract the last line
            lastline = symbol_df.tail(1)

            process_bb_overbought_logic(lastline,symbol,timeframe)
            process_bb_oversold_logic(lastline,symbol,timeframe)


            #symbol_df.to_csv(f"dump/{symbol}-{timeframe}-output.csv",sep='\t')
            time.sleep(0.95)
    time.sleep(5 * 60)
