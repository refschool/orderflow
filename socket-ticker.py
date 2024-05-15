#https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
#TODO : calculer le delta en fonction du temps , minute, 10 seconde, ou autres UT

import websocket,json,os
import cursor
cursor.hide()
last_closed = 0
last_time = 0 # millisecondes
max_impulse = 0

def on_message(ws, message):
    global last_closed, last_time,max_impulse
    """ convert string to dictionary"""
    message = json.loads(message)
    #print(message)
    time = message['E']
    candle = message['k']
    close = candle['c']
    pricedelta = float(close) - float(last_closed)
    timedelta = float(time) - float(last_time)
    impulse = pricedelta/ (timedelta/ 1000)
    if(abs(impulse) > abs(max_impulse)):
        max_impulse = impulse

    print("speed:USD/sec",round(impulse),"timedelta:",round(timedelta),"close:",close,"pricedelta:",round(pricedelta,2))
    print("current max impulse:",max_impulse)
    last_closed = close
    last_time = time


def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    ws.send('{"method":"SUBSCRIBE","params":["btcusdt@kline_1m"],"id":1}')


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(f"wss://stream.binance.com:9443/ws/btcusdt@kline_1m",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
#https://www.youtube.com/watch?v=d-2GoqQbagI