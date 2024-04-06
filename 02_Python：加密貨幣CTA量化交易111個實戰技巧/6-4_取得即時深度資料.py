import websocket
import json


def on_message(ws, message):
    msg = json.loads(message)
    print(msg)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_error(ws, error):
    print("### error ###")
    print(error)


symbol = 'ETHUSDT'
sockname = f'wss://fstream.binance.com/ws/{symbol.lower()}@bookTicker'
ws = websocket.WebSocketApp(sockname,
                            on_message=on_message,
                            on_close=on_close,
                            on_error=on_error)
ws.run_forever()


{
    "e": "bookTicker",         // event type
    "u": 400900217,            // order book updateId
    "E": 1568014460893,       // event time
    "T": 1568014460891,       // transaction time
    "s": "BNBUSDT",            // symbol
    "b": "25.35190000",        // best bid price
    "B": "31.21000000",        // best bid qty
    "a": "25.36520000",        // best ask price
    "A": "40.66000000" // best ask qty
}
