import binancelib as b

s1 = ('BTCUSDT',1000)
symbol,limit = s1

r = b.get_order_book(symbol,limit)

def convert_to_float(liste):
    liste[0] = float(liste[0])
    liste[1] = float(liste[1])
    return liste

def convert_orderbook_to_float(orderbook):
    new_orderbook = []
    for elem in orderbook:
        new_orderbook.append(convert_to_float(elem))
    return  new_orderbook


def aggregate_orderbook(orderbook,unit=0.1):
    """ sum by unit of x """
    nb_decimal = len(str(unit).split('.'))
    nb_decimal = 1
    new_orderbook = []
    """ trick to round up a decimal instead of default round down"""
    start_price = round(orderbook[0][0] , nb_decimal)
    qty = 0
    for item in orderbook:
        if item[0] > start_price - unit:
            qty = qty + item[1]
        else:
            """ add compounded ranges to new orderbook"""
            new_orderbook.append([start_price,round(qty)])
            """ start over """
            start_price = round(start_price - unit,nb_decimal)
            qty = item[1]
    return new_orderbook


bids = r['bids']
bids = convert_orderbook_to_float(bids)
for item in bids :
    print(item)

print("================")

new_orderbook = aggregate_orderbook(bids)
for item in new_orderbook:
    print(item)

"""
asks = r['asks'][::-1]
asks = convert_orderbook_to_float(asks)

print('asks')
print(asks)
print('bids')
"""
