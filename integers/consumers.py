import json
from time import sleep
import pandas as pd

from channels.generic.websocket import WebsocketConsumer
from .streaming import *

class WSConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        ticks = on_ticks(ws, ticks)
        for tick in ticks:
            self.send(json.dumps({'message':tick}))
            sleep(10)
