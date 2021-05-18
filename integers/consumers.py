import json
from time import sleep
import datetime
import pandas as pd

from channels.generic.websocket import WebsocketConsumer
from .streaming import *

class WSConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        def myconverter(o):
            if isinstance(o, datetime.datetime):
                return o.__str__()
        print("I M HEREEEEEEE")
        while True:
            self.send(json.dumps({'message':data[0]}, default = myconverter))
