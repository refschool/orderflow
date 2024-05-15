#https://python-binance.readthedocs.io/en/latest/market_data.html
# pip install python-binance
#https://testnet.binance.vision/
from binance.client import Client
import pandas as pd
import pprint

API_KEY = "apikey"
API_SECRET = "apisecret"

client = Client(API_KEY,API_SECRET,testnet=True)
candles = client.get_historical_klines('LTCUSDT','1h','10 day ago UTC')
pprint.pprint(candles)

# keep 5 columns only
for line in candles:
    del line[5:]

symbol_df = pd.DataFrame(candles, columns=['date','open','high','low','close'])

# compute SMA 20
period = 20
symbol_df['sma'] = symbol_df['close'].rolling(period).mean()
# std deviation
symbol_df['std'] = symbol_df['close'].rolling(period).std()

symbol_df['upper'] = symbol_df['sma']  + (2 * symbol_df['std'])
symbol_df['lower'] = symbol_df['sma']  - (2 * symbol_df['std'])

symbol_df.set_index('date',inplace=True)
symbol_df.index = pd.to_datetime(symbol_df.index,unit='ms')


#write to tsv
with open('output.txt','w') as file:
    file.write(symbol_df.to_string()
               )