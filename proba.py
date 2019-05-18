from websocket import WebSocketApp
from json import dumps, loads
from pprint import pprint
import numpy as np



URL = "wss://ws-feed.gdax.com"

def on_message(_, message):
    """Callback executed when a message comes.
    Positional argument:
    message -- The message itself (string)
    """
    global r_ask_BTCUSD, r_bid_BTCUSD, r_ask_ETHUSD, r_bid_ETHUSD, r_ask_ETHBTC, r_bid_ETHBTC, arbitrazs
    global time_ask_BTCUSD, time_bid_BTCUSD, time_ask_ETHUSD, time_bid_ETHUSD, time_ask_ETHBTC, time_bid_ETHBTC, time_all
    a = loads(message)
    #print(a)
    #if a['type']=='snapshot':
        #i=0
        #print('Snapshot arrived.')"""

    #if a['type']=='l2update':
        #i=i+1
        #print('Update arrived.', a['changes'][0][0], a['product_id'])
        #print(a)"""

    if a["type"]=="snapshot" and (a["product_id"]=="BTC-USD"):
       time_ask_BTCUSD, time_bid_BTCUSD, time_ask_ETHUSD, time_bid_ETHUSD, time_ask_ETHBTC, time_bid_ETHBTC, time_all = [], [], [], [], [], [], []
       r_ask_BTCUSD=[(float(a["asks"][i][0]), float(a['asks'][i][1])) for i in range(10)]
       r_bid_BTCUSD = [(float(a["bids"][i][0]), float(a['bids'][i][1])) for i in range(10)]

    if a["type"] == "snapshot" and (a["product_id"] == "ETH-BTC"):
        r_ask_ETHBTC = [(float(a["asks"][i][0]), float(a['asks'][i][1])) for i in range(10)]
        r_bid_ETHBTC = [(float(a["bids"][i][0]), float(a['bids'][i][1])) for i in range(10)]

    if a["type"] == "snapshot" and (a["product_id"] == "ETH-USD"):
        r_ask_ETHUSD = [(float(a["asks"][i][0]), float(a['asks'][i][1])) for i in range(10)]
        r_bid_ETHUSD = [(float(a["bids"][i][0]), float(a['bids'][i][1])) for i in range(10)]

    #print('Init : ', r_ask_BTCUSD)

    #-------------ORDERBOOK KIVONATOK------------------------------------------------------------
    #--------------------------------------------------------------------------------------------

    #--------------------------------------------------------------------------------------------
    #-------------BTC-USD frissítések------------------------------------------------------------

    if a["type"]=="l2update" and (a["product_id"]=="BTC-USD") and a["changes"][0][0]=="buy":
        #print('SHIT HAPPENS!')
        dtype = [('price', float), ('size', float)]
        for value in a['changes']:
            print(value)
            #print(len(r_ask_BTCUSD))
            if(float(value[2])==0):
                j=float(value[1])
                #print(j)
                for k in range(len(r_ask_BTCUSD)):
                    if (r_ask_BTCUSD[k][0]==j):
                        #print(r_ask_BTCUSD[k][0])
                        r_ask_BTCUSD.pop(k)

            else:
                r_ask_BTCUSD.append((float(value[1]), float(value[2])))
                time_ask_BTCUSD.append(a["time"])
        _r_ask_BTCUSD = np.array(r_ask_BTCUSD, dtype=dtype)
        _r_ask_BTCUSD = np.sort(_r_ask_BTCUSD, order='price')[::1]
        r_ask_BTCUSD = [_r_ask_BTCUSD[i] for i in range(10)]
        #print("ask")
        print(r_ask_BTCUSD)
        #print(value[2])
        #print(len(time_ask_BTCUSD))
        #print(time_ask_BTCUSD[0])
        #print(r_ask_BTCUSD)
        #print(_r_ask_BTCUSD)
        #print('On update 1 : ', r_ask_BTCUSD[0])
        #exit(1)


    if a["type"]=="l2update" and (a["product_id"]=="BTC-USD") and a["changes"][0][0]=="sell":
        dtype = [('price', float), ('size', float)]
        for value in a['changes']:
            r_bid_BTCUSD.append((float(value[1]), float(value[2])))
            time_bid_BTCUSD.append(a["time"])
        _r_bid_BTCUSD = np.array(r_bid_BTCUSD, dtype=dtype)
        _r_bid_BTCUSD = np.sort(_r_bid_BTCUSD, order='price')[::-1]
        r_bid_BTCUSD = [_r_bid_BTCUSD[i] for i in range(10)]
        #print("bid")
        #print(r_bid_BTCUSD)
        #print(time_bid_BTCUSD[0])
        #print(r_bid_BTCUSD)
        #print(_r_bid_BTCUSD)
        #print('On update 2 : ', r_bid_BTCUSD[0])
        #exit(1)

    #--------------------------------------------------------------------------------------------
    #-------------ETH-USD frissítések------------------------------------------------------------

    if a["type"]=="l2update" and (a["product_id"]=="ETH-USD") and a["changes"][0][0]=="buy":
        #print('SHIT HAPPENS!')
        dtype = [('price', float), ('size', float)]
        for value in a['changes']:
            #print(value)
            r_ask_ETHUSD.append((float(value[1]), float(value[2])))
            time_ask_ETHUSD.append(a["time"])
        _r_ask_ETHUSD = np.array(r_ask_ETHUSD, dtype=dtype)
        _r_ask_ETHUSD = np.sort(_r_ask_ETHUSD, order='price')[::1]
        r_ask_ETHUSD = [_r_ask_ETHUSD[i] for i in range(10)]
        #print(time_ask_ETHUSD[0])
        """print(r_ask_ETHUSD)
        print(_r_ask_ETHUSD)
        print('On update 2 : ', r_ask_ETHUSD[0])
        #exit(1)"""


    if a["type"]=="l2update" and (a["product_id"]=="ETH-USD") and a["changes"][0][0]=="sell":
        #print('SHIT HAPPENS!')
        dtype = [('price', float), ('size', float)]
        for value in a['changes']:
            #print(value)
            r_bid_ETHUSD.append((float(value[1]), float(value[2])))
            time_bid_ETHUSD.append(a["time"])
        _r_bid_ETHUSD = np.array(r_bid_ETHUSD, dtype=dtype)
        _r_bid_ETHUSD = np.sort(_r_bid_ETHUSD, order='price')[::-1]
        r_bid_ETHUSD = [_r_bid_ETHUSD[i] for i in range(10)]
        #print(time_bid_ETHUSD[0])
        #print(r_bid_ETHUSD)
        #print(_r_ask_ETHUSD)
        #print('On update 2 : ', r_ask_ETHUSD[0])
        #exit(1)

    #--------------------------------------------------------------------------------------------
    #-------------ETH-BTC frissítések------------------------------------------------------------

    if a["type"]=="l2update" and (a["product_id"]=="ETH-BTC") and a["changes"][0][0]=="buy":
        dtype = [('price', float), ('size', float)]
        for value in a['changes']:
            if (float(value[2])!=0):
                r_ask_ETHBTC.append((float(value[1]), float(value[2])))
                time_ask_ETHBTC.append(a["time"])
        _r_ask_ETHBTC = np.array(r_ask_ETHBTC, dtype=dtype)
        _r_ask_ETHBTC = np.sort(_r_ask_ETHBTC, order='price')[::1]
        r_ask_ETHBTC = [_r_ask_ETHBTC[i] for i in range(10)]
        #print(time_ask_ETHBTC[0])
        #print(r_ask_ETHBTC)
        #print(_r_ask_ETHBTC)
        #print('On update 2 : ', r_ask_ETHBTC[0])
        #exit(1)"""



    if a["type"]=="l2update" and (a["product_id"]=="ETH-BTC") and a["changes"][0][0]=="sell":
        #print('SHIT HAPPENS!')
        dtype = [('price', float), ('size', float)]
        for value in a['changes']:
            #print(value)
            r_bid_ETHBTC.append((float(value[1]), float(value[2])))
            time_bid_ETHBTC.append(a["time"])
        _r_bid_ETHBTC = np.array(r_bid_ETHBTC, dtype=dtype)
        _r_bid_ETHBTC = np.sort(_r_bid_ETHBTC, order='price')[::-1]
        r_bid_ETHBTC = [_r_bid_ETHBTC[i] for i in range(10)]

        #print(r_bid_ETHBTC)
        #print(_r_ask_ETHBTC)
        #print('On update 2 : ', r_ask_ETHBTC[0])
        #exit(1)


    #--------------------------------------------------------------------------------------------
    #-------------MŰVELETEK AZ ORDERBOOKKAL------------------------------------------------------------

    arbitrazs_1=1-((r_ask_ETHBTC[0][0]*r_bid_BTCUSD[0][0])/r_bid_ETHUSD[0][0])
    arbitrazs_2=1-(r_ask_ETHUSD[0][0]/(r_bid_ETHBTC[0][0]*r_bid_BTCUSD[0][0]))
    #print("%f \t %f \t %f \t %f \t %f \t %f \t %f \t %f" % (r_ask_BTCUSD[0][0], r_bid_BTCUSD[0][0], r_ask_ETHUSD[0][0], r_bid_ETHUSD[0][0], r_ask_ETHBTC[0][0], r_bid_ETHBTC[0][0], arbitrazs_1, arbitrazs_2))



def on_open(socket):
    """Callback executed at socket opening.
    Keyword argument:
    socket -- The websocket itself
    """
    params = {

    "type": "subscribe",
    "channels": [
        {
            "name": "level2",
            "product_ids": [
                "ETH-USD",
                "BTC-USD",
                "ETH-BTC"
            ],
        },
        ]
    }

    socket.send(dumps(params))

def main():
    """Main function."""
    ws = WebSocketApp(URL, on_open=on_open, on_message=on_message)
    ws.run_forever()

if __name__ == '__main__':
    main()
    #print(time_ask_BTCUSD[0], time_ask_BTCUSD[int(len(time_ask_BTCUSD)/3)], time_ask_BTCUSD[int(2*len(time_ask_BTCUSD)/3)], time_ask_BTCUSD[len(time_ask_BTCUSD)-1], i)
