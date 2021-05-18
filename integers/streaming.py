import logging
import time
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)
api_key = open('/home/akkey/Desktop/Django-projects/django-sockets/demo1/integers/api_key.txt', 'r').read()
access_token = "pt5vbS56ncUWLl2bqd5FjuH1oM4iJ7pp"
tokens = [5215745, 633601, 1195009, 779521, 758529, 1256193, 194561, 1837825, 952577, 1723649, 3930881, 4451329, 593665, 3431425, 2905857, 3771393, 3789569, 3463169, 381697, 54273, 415745, 2933761, 3580417, 49409, 3060993, 4464129, 3375873, 4574465, 636673, 3721473, 2796801]

data = []
kws = KiteTicker(api_key, access_token)
def on_ticks(ws, ticks):
    # logging.debug("Ticks: {}".format(ticks[0]))
    print("Hiiemowe")
    data.clear()
    # print(ticks[0])
    data.extend(ticks)


def on_connect(ws, response):
    print("hellooooooo")
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL, tokens)

def on_close(ws, code, reason):
    ws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

print ('Hiiiiiiiiiiiiiiiiii')
kws.connect(threaded= True, disable_ssl_verification=False)
print ('HIIIIIIIIIIIIII')

