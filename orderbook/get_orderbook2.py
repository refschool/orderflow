import binancelib as binlib
import warnings
from orderflow_func import *
import sys
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
"""this script will get the passive orders, combine it with panda"""

s1 = ('BEAMXUSDT',1500) #number and granularity
symbol,limit = s1
order_book = binlib.get_order_book(symbol,limit)


""" ASKS """
side = 'asks'

flow = order_book[side]
flow = convert_orderbook_to_float(flow)
df = pd.DataFrame(flow,columns=['price','qty'])
print(df)
step = 0.0001 # TODO : to make it dynamic   1/100
begin,end,df = get_extremum(df,side)
referential = get_referential(begin,end,step)

get_order_flow(df,referential,side)

""" BIDS """
side = 'bids'

flow = order_book[side]
flow = convert_orderbook_to_float(flow)
df = pd.DataFrame(flow,columns=['price','qty'])

begin,end,df = get_extremum(df,side)
referential = get_referential(begin,end,step)

get_order_flow(df,referential,side)


