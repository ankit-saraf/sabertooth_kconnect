import logging
import time
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)
api_key = open('/home/akkey/Desktop/Django-projects/django-sockets/demo1/integers/api_key.txt', 'r').read()
access_token = "pfFISiNRTzZCAt5fmKoQRRZ3fw37N66k"
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

def historical_data(self, instrument_token, from_date, to_date, interval, continuous=False, oi=False):
    
    print("in function")
    date_string_format = "%Y-%m-%d %H:%M:%S"
    from_date_string = from_date.strftime(date_string_format) if type(from_date) == datetime.datetime else from_date
    to_date_string = to_date.strftime(date_string_format) if type(to_date) == datetime.datetime else to_date
    data = self._get("market.historical", {
        "instrument_token": instrument_token,
        "from": from_date_string,
        "to": to_date_string,
        "interval": interval,
        "continuous": 1 if continuous else 0,
        "oi": 1 if oi else 0
    })
    print(data)
    return self._format_historical(data, oi)

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.historical_data = historical_data

print ('Hiiiiiiiiiiiiiiiiii')
kws.connect(threaded= True, disable_ssl_verification=False)
print ('HIIIIIIIIIIIIII')

