import json
from time import sleep
import datetime
import pandas as pd

from channels.generic.websocket import WebsocketConsumer
from .streaming import data

class WSConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        for tick in data:
            print("I M HEREEEEEEE")
            print(tick)
            self.send(json.dumps({'message':tick}, default = myconverter))
            sleep(10)
