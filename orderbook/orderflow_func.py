def printRed(skk): print("\033[91m {}\033[00m" .format(skk))
def printBlue(skk): print("\033[94m {}\033[00m" .format(skk))


def get_referential(begin,end,step):
    referential = []
    while begin >= end - step: #  -step necessary otherwise we miss one
        referential.append(round(begin,4))
        begin = begin - step

    return referential


def convert_to_float(liste):
    liste[0] = float(liste[0])
    liste[1] = float(liste[1])
    return liste

def convert_orderbook_to_float(orderbook: list) -> list:
    new_orderbook = []
    for elem in orderbook:
        new_orderbook.append(convert_to_float(elem))
    return new_orderbook


""" https://www.geeksforgeeks.org/print-colors-python-terminal/ """
def get_order_flow(df,referential,side):
    sum=0
    for index,row in df.iterrows():
        price = row['price']
        qty = row['qty']
        upper = referential[0]
        lower = referential[1]
        if(upper >= price > lower):
            sum= sum + qty
        if(lower >= price):
            """ special char question https://stackoverflow.com/questions/10635226/python-how-to-print-a-block-using-ascii-219-in-mac """
            """ TODO make denominator of sum variable"""
            phrase = f"sum {upper:.4f} > price > {lower:.4f}" + str(round(sum)).rjust(10) + ' ' +round(sum/100000) * u"\u2588"
            if(side=='asks'):
                printRed(phrase)
            else:
                printBlue(phrase)

            if(len(referential) > 2):
                referential = referential[1:]
                upper=lower
                lower=referential[1]
                sum = 0
            else:
                break

def get_extremum(df,side):
    """ reverse dataframe for the asks """
    if side == 'bids':
        begin =df['price'].iloc[0]
        end=df['price'].iloc[-1]
    else:
        df = df.iloc[::-1] #reverse dataframe
        begin =df['price'].iloc[0]
        end=df['price'].iloc[-1]
    return begin,end,df