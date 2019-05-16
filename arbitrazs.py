from pymongo import MongoClient
import time
import gdax
import numpy as np
mongo_client = MongoClient('mongodb://localhost:27017/')

# specify the database and collection
db = mongo_client.cryptocurrency_database
BTC_collection = db.BTC_collection

# instantiate a WebsocketClient instance, with a Mongo collection as a parameter
"""wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products="BTC-USD")
wsClient.start()
time.sleep(20)
wsClient.close()
"""

myfile=open("arbit1.txt", "r")
lines = myfile.read().split('(')
print (lines)
print(len(lines))









    



